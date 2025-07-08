#!/usr/bin/env python3
import json
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Generate a VDR (Vulnerability Disclosure Report) JSON by merging SBOM and vulnerability scan results."
    )
    parser.add_argument("sbom_file", help="Input SBOM JSON file (CycloneDX format).")
    parser.add_argument("vuln_file", help="Input vulnerabilities JSON file (Trivy scan result).")
    parser.add_argument("output_file", help="Output VDR JSON file.")

    parser.add_argument("--author", default="Your Name or Org",
                        help="Author of the VDR report. The name of the individual or team generating this VDR.")
    parser.add_argument("--publisher-name", default="Your Organization",
                        help="Publisher organization name. The organization publishing this report.")
    parser.add_argument("--publisher-url", default="https://yourorg.example.com",
                        help="Publisher organization URL. The website URL of the publisher organization.")
    parser.add_argument("--contact-name", default="Security Team",
                        help="Contact person or team name responsible for this report.")
    parser.add_argument("--contact-email", default="security@example.com",
                        help="Contact email address for security inquiries.")
    parser.add_argument("--audience-name", default="IBM Concert Upload",
                        help="Audience name. Intended recipient or system for this report.")
    parser.add_argument("--audience-type", default="service",
                        help="Audience type, such as 'service' or 'team'.")
    parser.add_argument("--scan-type", default="source",
                        help="Type of scan, such as 'source' or 'image'. Used as a custom property for parsing in Concert.")

    args = parser.parse_args()

    # Load SBOM
    with open(args.sbom_file, 'r') as f:
        sbom_data = json.load(f)

    # Load vulnerabilities file
    with open(args.vuln_file, 'r') as f:
        vuln_data = json.load(f)

    # Set schema to VDR schema
    sbom_data['$schema'] = 'http://cyclonedx.org/schema/ext/vulnerability-disclosure/1.0'

    # Parse vulnerabilities
    vulnerabilities = []
    if 'Results' in vuln_data:
        for result in vuln_data['Results']:
            if 'Vulnerabilities' in result and result['Vulnerabilities']:
                for v in result['Vulnerabilities']:
                    vuln_entry = {
                        "id": v.get("VulnerabilityID"),
                        "source": {
                            "name": v.get("SeveritySource"),
                            "url": v.get("PrimaryURL")
                        },
                        "ratings": [
                            {
                                "severity": v.get("Severity").lower()
                            }
                        ],
                        "description": v.get("Description"),
                        "affects": [
                            {
                                "ref": v.get("PkgIdentifier", {}).get("PURL", "")
                            }
                        ]
                    }
                    vulnerabilities.append(vuln_entry)

    if vulnerabilities:
        sbom_data['vulnerabilities'] = vulnerabilities
    else:
        print("No vulnerabilities found in vuln_file.")

    # Add scan.type property to metadata.component
    if 'metadata' in sbom_data and 'component' in sbom_data['metadata']:
        sbom_data['metadata']['component'].setdefault('properties', []).append({
            "name": "scan.type",
            "value": args.scan_type
        })

    # Add metadata.vdr block
    sbom_data.setdefault('metadata', {})
    sbom_data['metadata']['vdr'] = {
        "author": args.author,
        "publisher": {
            "name": args.publisher_name,
            "url": args.publisher_url
        },
        "contact": [
            {
                "name": args.contact_name,
                "email": args.contact_email
            }
        ],
        "audience": [
            {
                "name": args.audience_name,
                "type": args.audience_type
            }
        ]
    }

    # Output VDR JSON
    with open(args.output_file, 'w') as f:
        json.dump(sbom_data, f, indent=2)

    print(f"✅ VDR file generated: {args.output_file}")

if __name__ == "__main__":
    main()

