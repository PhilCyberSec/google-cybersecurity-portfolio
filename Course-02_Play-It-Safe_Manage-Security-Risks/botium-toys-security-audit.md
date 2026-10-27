# Botium Toys: Combined Security Audit Documentation



---

## 1. Scenario

Review the following scenario. Then complete the step-by-step instructions.

This scenario is based on a fictional company:

Botium Toys is a small U.S. business that develops and sells toys. The business has a single physical location, which serves as their main office, a storefront, and warehouse for their products. However, Botium Toys’ online presence has grown, attracting customers in the U.S. and abroad. As a result, their information technology (IT) department is under increasing pressure to support their online market worldwide.

The manager of the IT department has decided that an internal IT audit needs to be conducted. She is worried about maintaining compliance and business operations as the company grows without a clear plan. She believes an internal audit can help better secure the company’s infrastructure and help them identify and mitigate potential risks, threats, or vulnerabilities to critical assets. The manager is also interested in ensuring that they comply with regulations related to internally processing and accepting online payments and conducting business in the European Union (E.U.).

The IT manager starts by implementing the National Institute of Standards and Technology Cybersecurity Framework (NIST CSF), establishing an audit scope and goals, listing assets currently managed by the IT department, and completing a risk assessment. The goal of the audit is to provide an overview of the risks and/or fines that the company might experience due to the current state of their security posture.

Your task is to review the IT manager’s scope, goals, and risk assessment report. Then, perform an internal audit by completing a controls and compliance checklist.

---

## 2. Botium Toys: Scope, Goals, and Risk Assessment Report



### Scope and Goals of the Audit

Scope:
- The scope of this audit is defined as the entire security program at Botium Toys.
- This includes their assets like employee equipment and devices, their internal network, and their systems.
- The audit requires review of the assets Botium Toys has and the controls and compliance practices they have in place.

Goals:
- Assess existing assets and complete the controls and compliance checklist.
- Determine which controls and compliance best practices need to be implemented to improve Botium Toys’ security posture.

### Current Assets

Assets managed by the IT Department include:
- On-premises equipment for in-office business needs
- Employee equipment: end-user devices (desktops/laptops, smartphones), remote workstations, headsets, cables, keyboards, mice, docking stations, surveillance cameras, etc.
- Storefront products available for retail sale on site and online; stored in the company’s adjoining warehouse
- Management of systems, software, and services: accounting, telecommunication, database, security, ecommerce, and inventory management
- Internet access
- Internal network
- Data retention and storage
- Legacy system maintenance: end-of-life systems that require human monitoring

### Risk Assessment

#### Risk Description
Currently, there is inadequate management of assets. Additionally, Botium Toys does not have all of the proper controls in place and may not be fully compliant with U.S. and international regulations and standards.

#### Control Best Practices
The first of the five functions of the NIST CSF is Identify. Botium Toys will need to dedicate resources to identify assets so they can appropriately manage them. Additionally, they will need to classify existing assets and determine the impact of the loss of existing assets, including systems, on business continuity.

#### Risk Score
On a scale of 1 to 10, the risk score is 8, which is fairly high. This is due to a lack of controls and adherence to compliance best practices.

#### Additional Comments
The potential impact from the loss of an asset is rated as medium, because the IT department does not know which assets would be at risk. The risk to assets or fines from governing bodies is high because Botium Toys does not have all of the necessary controls in place and is not fully adhering to best practices related to compliance regulations that keep critical data private/secure.

Specific details:
- Currently, all Botium Toys employees have access to internally stored data and may be able to access cardholder data and customers’ PII/SPII.
- Encryption is not currently used to ensure confidentiality of customers’ credit card information that is accepted, processed, transmitted, and stored locally in the company’s internal database.
- Access controls pertaining to least privilege and separation of duties have not been implemented.
- The IT department has ensured availability and integrated controls to ensure data integrity.
- The IT department has a firewall that blocks traffic based on an appropriately defined set of security rules.
- Antivirus software is installed and monitored regularly by the IT department.
- The IT department has not installed an intrusion detection system (IDS).
- There are no disaster recovery plans currently in place, and the company does not have backups of critical data.
- The IT department has established a plan to notify E.U. customers within 72 hours if there is a security breach. Additionally, privacy policies, procedures, and processes have been developed and are enforced among IT department members/other employees to properly document and maintain data.
- Although a password policy exists, its requirements are nominal and not in line with current minimum password complexity requirements (for example, at least eight characters, a combination of letters and at least one number; special characters).
- There is no centralized password management system that enforces the password policy’s minimum requirements, which sometimes affects productivity when employees/vendors submit a ticket to the IT department to recover or reset a password.
- While legacy systems are monitored and maintained, there is no regular schedule in place for these tasks and intervention methods are unclear.
- The store’s physical location, which includes Botium Toys’ main offices, storefront, and warehouse of products, has sufficient locks, up-to-date closed-circuit television (CCTV) surveillance, as well as functioning fire detection and prevention systems.

---

## 3. Control Categories

Controls within cybersecurity are grouped into three main categories:
- Administrative/Managerial controls
- Technical controls
- Physical/Operational controls

### Administrative/Managerial Controls
Administrative/Managerial controls address the human component of cybersecurity. These controls include policies and procedures that define how an organization manages data and clearly defines employee responsibilities, including their role in protecting the organization. While administrative controls are typically policy-based, the enforcement of those policies may require the use of technical or physical controls.

| Control Name | Control Type | Control Purpose |
|---|---|---|
| Least Privilege | Preventative | Reduce risk and overall impact of malicious insider or compromised accounts |
| Disaster Recovery Plans | Corrective | Provide business continuity |
| Password Policies | Preventative | Reduce likelihood of account compromise through brute force or dictionary attack techniques |
| Access Control Policies | Preventative | Bolster confidentiality and integrity by defining which groups can access or modify data |
| Account Management Policies | Preventative | Managing account lifecycle, reducing attack surface, and limiting overall impact from disgruntled former employees and default account usage |
| Separation of Duties | Preventative | Reduce risk and overall impact of malicious insider or compromised accounts |

### Technical Controls
Technical controls consist of solutions such as firewalls, intrusion detection systems (IDS), intrusion prevention systems (IPS), antivirus (AV) products, encryption, etc. Technical controls can be used in a number of ways to meet organizational goals and objectives.

| Control Name | Control Type | Control Purpose |
|---|---|---|
| Firewall | Preventative | Filter unwanted or malicious traffic from entering the network |
| IDS/IPS | Detective | Detect and prevent anomalous traffic that matches a signature or rule |
| Encryption | Deterrent | Provide confidentiality to sensitive information |
| Backups | Corrective | Restore/recover from an event |
| Password Management | Preventative | Reduce password fatigue |
| Antivirus (AV) Software | Preventative | Scan to detect and quarantine known threats |
| Manual Monitoring, Maintenance, and Intervention | Preventative | Identify and manage threats, risks, or vulnerabilities to out-of-date systems |

### Physical/Operational Controls
Physical/Operational controls include door locks, cabinet locks, surveillance cameras, badge readers, etc. They are used to limit physical access to physical assets by unauthorized personnel.

| Control Name | Control Type | Control Purpose |
|---|---|---|
| Time-Controlled Safe | Deterrent | Reduce attack surface and overall impact from physical threats |
| Adequate Lighting | Deterrent | Deter threats by limiting hiding places |
| Closed-Circuit Television (CCTV) | Preventative/Detective | Reduce the likelihood of certain events and provide evidence after an event |
| Locking Cabinets (for network gear) | Preventative | Bolster integrity by preventing unauthorized persons from physically accessing or modifying network gear |
| Signage Indicating Alarm Service Provider | Deterrent | Deter certain types of threats |
| Locks | Deterrent/Preventative | Bolster integrity by deterring and preventing unauthorized access |
| Fire Detection and Prevention | Detective/Preventative | Detect fire in a physical location and prevent damage to physical assets |

### Control Types
Control types include, but are not limited to:
1. Preventative
2. Corrective
3. Detective
4. Deterrent

These controls work together to provide defense in depth and protect assets.
- Preventative controls are designed to prevent an incident from occurring in the first place.
- Corrective controls are used to restore an asset after an incident.
- Detective controls are implemented to determine whether an incident has occurred or is in progress.
- Deterrent controls are designed to discourage attacks.

---

## 4. Controls and Compliance Checklist

To complete the controls assessment checklist, refer to the information provided in the scope, goals, and risk assessment report. For more details about each control, including the type and purpose, refer to the control categories document. Then, select “yes” or “no” to answer the question: Does Botium Toys currently have this control in place?

### Controls Assessment Checklist

- Least Privilege: Yes / No
- Disaster Recovery Plans: Yes / No
- Password Policies: Yes / No
- Separation of Duties: Yes / No
- Firewall: Yes / No
- Intrusion Detection System (IDS): Yes / No
- Backups: Yes / No
- Antivirus Software: Yes / No
- Manual Monitoring, Maintenance, and Intervention for Legacy Systems: Yes / No
- Encryption: Yes / No
- Password Management System: Yes / No
- Locks (offices, storefront, warehouse): Yes / No
- Closed-Circuit Television (CCTV) Surveillance: Yes / No
- Fire Detection/Prevention (fire alarm, sprinkler system, etc.): Yes / No

To complete the compliance checklist, refer to the information provided in the scope, goals, and risk assessment report. For more details about each compliance regulation, review the controls, frameworks, and compliance reading. Then, select “yes” or “no” to answer the question: Does Botium Toys currently adhere to this compliance best practice?

### Compliance Checklist

#### Payment Card Industry Data Security Standard (PCI DSS)
- Only authorized users have access to customers’ credit card information. Yes / No
- Credit card information is stored, accepted, processed, and transmitted internally in a secure environment. Yes / No
- Implement data encryption procedures to better secure credit card transaction touchpoints and data. Yes / No
- Adopt secure password management policies. Yes / No

#### General Data Protection Regulation (GDPR)
- E.U. customers’ data is kept private/secured. Yes / No
- There is a plan in place to notify E.U. customers within 72 hours if their data is compromised or there is a breach. Yes / No
- Ensure data is properly classified and inventoried. Yes / No
- Enforce privacy policies, procedures, and processes to properly document and maintain data. Yes / No

#### System and Organizations Controls (SOC Type 1, SOC Type 2)
- User access policies are established. Yes / No
- Sensitive data (PII/SPII) is confidential/private. Yes / No
- Data integrity ensures the data is consistent, complete, accurate, and has been validated. Yes / No
- Data is available to individuals authorized to access it. Yes / No

### Recommendations
This section is optional and can be used to provide a summary of recommendations to the IT manager regarding which controls and/or compliance best practices Botium Toys needs to implement, based on the risk posed if not implemented in a timely manner.

Recommendations from the report:

#### Critical (Immediate Action Required)
- Adopt least privilege access and separation of duties principles — all personnel currently have unlimited access to all types of information stored on company databases, including cardholder data and any other personally identifiable and sensitive personally identifiable information.
- Encrypt credit card data in rest and on transmission to comply with PCI DSS standards.
- Implement an IDS to protect networks from suspicious activity.
- Create a disaster recovery plan and backup company data.

#### High Priority
- Replace the old password policy with more secure and complex password requirements and implement a password management solution.
- Conduct asset classification and inventorying to determine what types of information are stored in company systems, where this data is located, and what consequences its loss can bring.

#### Moderately Urgent Priority
- Develop a routine for monitoring legacy systems and establish intervention processes that will minimize confusion and human errors.
- Classify and protect all customer data for E.U. clients in compliance with GDPR.
- Physical controls (locks, cameras, fire detectors) are all installed and do not need any further actions.

---

## 5. Summary

This activity is designed to evaluate how well the organization’s current controls, risk posture, and compliance practices align with the needs of a growing online retail business. The internal audit focuses on identifying gaps in security controls, regulatory readiness, and operational resilience while helping the IT department prioritize improvements.
