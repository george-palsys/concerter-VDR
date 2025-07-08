# generate\_vdr.py

## Overview

This script merges a **CycloneDX SBOM JSON** file with a **Trivy vulnerability scan result JSON** to produce a **Vulnerability Disclosure Report (VDR)** in CycloneDX VDR schema format. This is useful for tools like **IBM Concert** that require VDR inputs to display vulnerabilities linked to SBOM components.

---

## Usage

```bash
python generate_vdr.py <sbom_file> <vuln_file> <output_file> [options]
```

### Positional arguments

| Argument      | Description                                          |
| ------------- | ---------------------------------------------------- |
| `sbom_file`   | Input SBOM JSON file (CycloneDX format).             |
| `vuln_file`   | Input vulnerabilities JSON file (Trivy scan result). |
| `output_file` | Output VDR JSON file.                                |

---

### Optional parameters

| Option             | Default                                                    | Description                                                                       |
| ------------------ | ---------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `--author`         | Your Name or Org                                           | Author of the VDR report. The name of the individual or team generating this VDR. |
| `--publisher-name` | Your Organization                                          | Publisher organization name. The organization publishing this report.             |
| `--publisher-url`  | [https://yourorg.example.com](https://yourorg.example.com) | Publisher organization URL. The website URL of the publisher organization.        |
| `--contact-name`   | Security Team                                              | Contact person or team name responsible for this report.                          |
| `--contact-email`  | [security@example.com](mailto:security@example.com)        | Contact email address for security inquiries.                                     |
| `--audience-name`  | IBM Concert Upload                                         | Audience name. Intended recipient or system for this report.                      |
| `--audience-type`  | service                                                    | Audience type, such as 'service' or 'team'.                                       |

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
  --audience-type "service"
```

---

## Notes

* Ensure the **vulnerability scan result JSON** (`vuln_file`) is generated using Trivy with `--format json`.
* The output VDR JSON file can then be uploaded to **IBM Concert** or other SBOM+vulnerability management platforms that support CycloneDX VDR schema.

---

