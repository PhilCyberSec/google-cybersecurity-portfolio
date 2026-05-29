# Incident Handler's Journal

**Analyst:** [Your Name]  
**Date Started:** [Date]

This journal documents security incidents investigated during the Google Cybersecurity Certificate program. Each entry follows the 5 W's framework: Who, What, Where, When, and Why.

---

## Entry 1

**Date:** [Date]  
**Entry:** 1

### Description

A small U.S. health care clinic experienced a ransomware attack that encrypted all files on company computers. The attack was delivered via phishing emails containing malicious attachments. Employees accidentally downloaded the attachment, triggering the ransomware. Attackers demanded a large ransom in exchange for the decryption key.

### The 5 W's

| Field | Details |
|-------|---------|
| **Who** | Organised group of unethical hackers known to target healthcare and transportation sectors |
| **What** | Ransomware attack via phishing emails; all files encrypted; ransom demanded |
| **Where** | Small U.S. health care clinic |
| **When** | Tuesday morning, start of business day |
| **Why** | Employees clicked malicious phishing email attachments, executing ransomware payload |

### Additional Notes

- Business operations were severely disrupted; critical medical records unavailable
- The organisation did not have backups in place, increasing the pressure to pay the ransom
- **Recommendation:** Implement regular security awareness training, robust email filtering, and tested backup/recovery procedures

---

## Entry 2

**Date:** [Date]  
**Entry:** 2

### Description

Investigated a suspicious file hash using VirusTotal as part of an alert raised by a SIEM tool. A file with SHA-256 hash `54e6ea47eb04634d3e87fd7787e2136ccfbcc80ade34f246a12cf93bab527f6b` was flagged by multiple antivirus engines as malicious.

### The 5 W's

| Field | Details |
|-------|---------|
| **Who** | Unknown threat actor; malware identified as a known family |
| **What** | Malicious file detected on an internal endpoint; confirmed malware via VirusTotal |
| **Where** | Internal employee workstation |
| **When** | Detected by SIEM alert during business hours |
| **Why** | File was likely introduced via a drive-by download or malicious email attachment |

### Additional Notes

- File hash confirmed malicious by 58 of 72 security vendors on VirusTotal
- Endpoint was isolated and reimaged; user credentials reset
- Correlated with known indicators of compromise (IOCs) from threat intelligence feeds

---

## Entry 3

**Date:** [Date]  
**Entry:** 3

### Description

Analysed a packet capture file to investigate suspicious network traffic. Used Wireshark to identify a potential DNS exfiltration attempt, with unusually long DNS query names containing encoded data.

### The 5 W's

| Field | Details |
|-------|---------|
| **Who** | Internal host `192.168.1.105` communicating with external DNS server |
| **What** | Anomalous DNS queries with encoded subdomains suggestive of data exfiltration |
| **Where** | Internal network segment |
| **When** | Overnight, outside business hours |
| **Why** | Possible malware using DNS tunnelling to exfiltrate data covertly |

### Additional Notes

- DNS query lengths significantly exceeded normal thresholds
- Queries directed to an unregistered external domain
- Recommended: block the external domain, investigate the affected host, review DNS traffic monitoring rules

---

## Reflections

Through these journal entries, I have developed a structured approach to incident documentation. Recording the 5 W's for each incident ensures that investigations are thorough, reproducible, and useful for future reference. Clear documentation is essential for effective communication with stakeholders and for informing post-incident remediation efforts.
