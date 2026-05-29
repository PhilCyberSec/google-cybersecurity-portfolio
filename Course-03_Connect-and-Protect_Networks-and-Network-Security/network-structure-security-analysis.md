# Network Structure and Security Analysis

**Company:** Social Media Organization (fictional scenario)  
**Date:** [Date]  
**Analyst:** [Your Name]

---

## Scenario Summary

A social media organization experienced a major data breach. The attacker gained unauthorized access through the company's web application, exploiting brute force techniques to access administrative accounts. Upon gaining access, the attacker changed security settings and locked out administrators. The organization needs to assess its current security posture and implement improvements.

---

## NIST CSF Analysis

### 1. Identify

**Current Network Structure:**
- Thousands of customer records were compromised, including names, addresses, phone numbers, and email addresses.
- The organization's network connects employees to internal databases containing customer data.
- Access management policies were insufficiently enforced, allowing brute-force attacks to succeed.

**Identified Vulnerabilities:**
- No multi-factor authentication (MFA) on administrative accounts
- Insufficient account lockout policies
- Overly permissive access controls
- No dedicated intrusion detection system

---

### 2. Protect

**Recommended Protections:**

| Control | Description |
|---------|-------------|
| Multi-Factor Authentication (MFA) | Require MFA for all administrative and privileged accounts |
| Strong password policy | Enforce complex passwords with regular rotation |
| Account lockout | Implement lockout after a defined number of failed login attempts |
| Role-Based Access Control (RBAC) | Limit access to sensitive data to authorized personnel only |
| Network segmentation | Isolate databases from general internal network traffic |

---

### 3. Detect

**Recommended Detection Measures:**

- Deploy a **SIEM tool** to aggregate and analyze logs for suspicious activity
- Implement an **Intrusion Detection System (IDS)** to alert on anomalous login behaviour
- Establish **baseline thresholds** for login attempts to detect brute-force activity
- Monitor network traffic for unusual data exfiltration patterns

---

### 4. Respond

**Incident Response Improvements:**

- Develop and maintain a formal **Incident Response Plan (IRP)**
- Define escalation paths and communication protocols for security incidents
- Conduct quarterly **tabletop exercises** to practice incident response
- Establish a process for notifying affected customers and regulators within required timeframes (e.g., GDPR 72-hour rule)

---

### 5. Recover

**Recovery Recommendations:**

- Restore affected systems from **verified, clean backups**
- Reset all administrative credentials and review all access following the incident
- Conduct a **post-incident review** to identify lessons learned
- Update the incident response plan based on findings
- Communicate recovery status transparently with stakeholders

---

## Summary

This analysis reveals significant gaps in the organization's network security posture, particularly around access control, detection, and incident response. Immediate priorities should include implementing MFA, deploying an IDS/SIEM, and developing a formal incident response plan. Longer-term, network segmentation and regular security assessments will strengthen the overall security posture.
