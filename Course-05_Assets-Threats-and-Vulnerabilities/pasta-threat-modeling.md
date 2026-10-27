# PASTA Threat Modeling Activity

> Note: Leave the original PDF/template as it is. This markdown file contains the full assignment context, instructions, and the relevant supporting content in one place for easier review and portfolio use.

---

## Activity Overview

In this activity, you will practice using the Process of Attack Simulation and Threat Analysis (PASTA) threat model framework. You will determine whether a new shopping app is safe to launch.

Threat modeling is an important part of secure software development. Security teams typically perform threat models to identify vulnerabilities before malicious actors do. PASTA is a commonly used framework for assessing the risk profile of new applications.

---

## Scenario

Review the following scenario. Then complete the step-by-step instructions.

You’re part of the growing security team at a company for sneaker enthusiasts and collectors. The business is preparing to launch a mobile app that makes it easy for their customers to buy and sell shoes.

You are performing a threat model of the application using the PASTA framework. You will go through each of the seven stages of the framework to identify security requirements for the new sneaker company app.

---

## Step-by-Step Instructions

Follow the instructions and answer the included questions to complete the activity.

### Part 1 - Access the Resources

To use the template for this course item, click the following link and select Use Template.

- Template: PASTA worksheet

The following supporting materials will help you complete this activity. Keep them open as you proceed to the next steps.

- Supporting materials: PASTA data flow diagram and PASTA attack tree

### Part 2 - Complete the PASTA Stages

#### Stage I: Business Objectives
The main goal of Stage I is to understand why the application was developed and what it is expected to do.

Note: Stage I typically requires gathering input from many individuals at a business.

First, review the following description of why the sneaker company decided to develop this new app:

Description:
- The application should seamlessly connect sellers and shoppers.
- It should be easy for users to sign up, log in, and manage their accounts.
- Data privacy is a big concern.
- Buyers should be able to directly message sellers with questions.
- They should also be able to rate sellers to encourage good service.
- Sales should be clear and quick to process.
- Users should have several payment options for a smooth checkout process.
- Proper payment handling is important because we want to avoid legal issues.

In the Stage I row of the PASTA worksheet, make 2–3 notes of business objectives identified from this description.

Possible business objectives:
- Secure account creation, login, and account management
- Protect user privacy and personal information
- Enable safe buying, selling, messaging, and payment processing

#### Stage II: Technological Scope
In Stage II, the technological scope of the project is defined. Normally, the application development team is involved because they have the most knowledge about the code base and application logic. As a security professional, your responsibility is to evaluate the application’s architecture for security risks.

The app will be exchanging and storing a lot of user data. These are some of the technologies it uses:

- Application programming interface (API): a set of rules that define how software components interact with each other.
- Public key infrastructure (PKI): an encryption framework that secures online information exchange.
- AES and RSA: symmetric and asymmetric encryption algorithms used to protect sensitive data and exchange keys.
- SHA-256: a hash function used to protect sensitive user data such as passwords and credit card numbers.
- SQL: a language used to store and retrieve data from a database.

Consider what you’ve learned about these technologies:
- Which would you evaluate first?
- How might they present security risks?

In the Stage II row, write 2–3 sentences (40–60 words) describing why you would prioritize a specific technology.

Example technology priority:
- I would prioritize payment handling and PKI encryption first because the app processes sensitive user and payment data.
- If these protections fail, the company could face legal issues, financial loss, and damage to customer trust.
- PKI, AES, and RSA help protect data in transit and at rest, which is critical for confidentiality and integrity.

#### Stage III: Data Flow Analysis
During Stage III, the objective is to analyze how the application is handling information. Here, each process is broken down.

For example, one process might be allowing buyers to search the database for shoes that are for sale.

Open the PASTA data flow diagram resource. Review the diagram and consider how the technologies relate to protecting user data during this process.

Important data flow points:
- User login and account access
- Search and listing retrieval from the database
- Buyer-seller messaging
- Purchase and payment processing
- Storage of customer and transaction information

#### Stage IV: Threat Identification
Stage IV is about identifying potential threats to the application, including threats to the technologies listed in Stage II and the processes shown in the data flow diagram.

For example, the app’s authentication system could be attacked with malware or social engineering.

In the Stage IV row of the PASTA worksheet, list 2 types of threats that are risks to the information being handled by the app.

Examples:
- Credential theft or account takeover
- Denial-of-service attacks that disrupt the app
- Malware or malicious code injection
- Social engineering attacks against employees or users

#### Stage V: Vulnerability Analysis
Stage V is the vulnerability analysis step. Here, you need to consider the attack surface of the technologies listed in Stage II.

For example, the app will use a payment system and the form used to collect credit card information might be vulnerable if it fails to encrypt data.

In Stage V, list 2 types of vulnerabilities that could be exploited.

Examples:
- SQL injection in database queries
- Weak authentication or poor password controls
- Insecure API endpoints or lack of authentication
- Unencrypted or poorly protected payment data

#### Stage VI: Attack Tree
Stage VI uses the information gathered in the previous two steps to build an attack tree.

Open the PASTA attack tree resource and review how threat actors could potentially exploit attack vectors.

Applications like this normally have large, complex attack trees with many branches.

Examples of attack paths:
- Attack a user account to gain access to personal or payment information
- Exploit an API or database weakness to access seller and buyer records
- Abuse messaging or profile access to collect sensitive data
- Use a payment form vulnerability to steal credit card information

#### Stage VII: Defenses and Safeguards
PASTA threat modeling is used to reduce the likelihood of security risks. In Stage VII, the final goal is to implement defenses and safeguards that mitigate threats.

In the Stage VII row of the PASTA worksheet, list 4 security controls that can reduce the chances of a security incident.

Examples of relevant controls:
- Multi-factor authentication (MFA)
- Encryption with PKI and secure key management
- Input validation and sanitization to prevent SQL injection
- Least privilege access controls
- Secure API authentication and rate limiting
- Logging, monitoring, and regular security testing

---

## What to Include in Your Response

Be sure to address the following elements:

- 2–3 business objectives
- 2–3 technology requirements or prioritization notes
- 2 potential threats
- 2 system vulnerabilities
- 4 defenses that limit risk

---

## Summary

This activity focuses on identifying security requirements for a new mobile shopping app using the PASTA framework. The goal is to assess business risk, analyze the technologies involved, identify likely threats and vulnerabilities, and recommend controls that reduce exposure before launch.
