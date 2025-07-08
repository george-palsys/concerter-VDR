# generate_vdr.py README.md

## Overview

This script merges a **CycloneDX SBOM JSON** file with a **Trivy vulnerability scan result JSON** to produce a **Vulnerability Disclosure Report (VDR)** in CycloneDX VDR schema format. It now also supports specifying a `--scan-type` parameter to indicate whether the scan is of a **source code repository** or a **container image**, useful for correct classification in IBM Concert.

---

## Usage

```bash
python generate_vdr.py <sbom_file> <vuln_file> <output_file> [options]
```

### Positional arguments

| Argument | Description |
|---|---|
| `sbom_file` | Input SBOM JSON file (CycloneDX format). |
| `vuln_file` | Input vulnerabilities JSON file (Trivy scan result). |
| `output_file` | Output VDR JSON file. |

---

### Optional parameters

| Option | Default | Description |
|---|---|---|
| `--author` | Your Name or Org | Author of the VDR report. |
| `--publisher-name` | Your Organization | Publisher organization name. |
| `--publisher-url` | https://yourorg.example.com | Publisher organization URL. |
| `--contact-name` | Security Team | Contact person or team name. |
| `--contact-email` | security@example.com | Contact email address. |
| `--audience-name` | IBM Concert Upload | Audience name, intended recipient or system for this report. |
| `--audience-type` | service | Audience type, such as 'service' or 'team'. |
| `--scan-type` | source | Type of scan, such as 'source' or 'image'. This is added as a custom property in the metadata for tools like IBM Concert to classify the scan correctly. |

---

## Example

```bash
python generate_vdr.py sbom.json vuln.json output_vdr.json \
  --author "DevSecOps Team" \
  --publisher-name "MyOrg" \
  --publisher-url "https://myorg.example.com" \
  --contact-name "Security Ops" \
  --contact-email "secops@myorg.com" \
  --audience-name "IBM Concert Upload" \
  --audience-type "service" \
  --scan-type source
```

---

## Notes

- If `--scan-type` is not specified, it defaults to `source`.
- The output VDR JSON file can then be uploaded to **IBM Concert** or other SBOM + vulnerability management platforms that support CycloneDX VDR schema.

---

Let me know if you also need a pipeline integration snippet for your upcoming implementation this week.

