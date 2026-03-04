# Sentinel SecureWorks
---
## Overview

Sentinel SecureWorks is an AI-assisted system designed to automate the process of completing structured security and compliance questionnaires using internal documentation as the source of truth.

Security teams frequently receive vendor security assessments, compliance questionnaires, and operational audits. These documents require answers grounded in internal policies and infrastructure documentation. Manually completing them is repetitive, slow, and error-prone.

This system demonstrates how AI can assist that workflow while keeping answers grounded in verified reference material.

The application parses questionnaires, retrieves relevant content from reference documents, generates answers with citations, allows human review, and exports the final structured response document.

Live Application Render Link (working link): 
https://sentinel-secureworks.onrender.com/


## Industry Context

Industry: Cybersecurity / Compliance Automation (SaaS)

Security vendors and SaaS companies routinely receive vendor risk assessments, security questionnaires, and compliance forms from potential customers. These documents require answers sourced from internal security documentation.

Automation in this space helps security teams reduce repetitive manual work while maintaining compliance accuracy.

## Fictional Company

Sentinel SecureWorks is a fictional cybersecurity SaaS company providing enterprise-grade security monitoring and compliance automation tools. The platform enables organizations to maintain strong security posture, streamline vendor risk assessments, and automate internal compliance documentation workflows.

## Problem Statement

Security questionnaires often contain dozens or hundreds of repetitive questions such as:

- Do you encrypt customer data at rest
- What authentication mechanisms are enforced?
- Do you maintain SOC 2 certification?

Answering these requires manually searching across multiple documents such as:

- Security policies
- Infrastructure documentation
- Compliance reports
- Operational procedures

This project demonstrates a system that automates this workflow while ensuring answers remain grounded in reference documentation.

## System Capabilities

The system performs the following workflow:

- Parses structured questionnaires into individual questions
- Retrieves relevant content from reference documentation
- Uses an LLM to generate grounded answers
- Attaches citations from reference sources
- Allows human review and editing
- Exports the completed questionnaire as a structured document

## Core Features

- User Authentication
- Questionnaire Upload
- Reference Document Upload
- AI Answer Generation
- Grounded Citations
- Unsupported Questions Handling
- Review & Edit Workflow
- Review & Edit Workflow

Nice to Have features implemented:

- Structured Export
- Confidence Score

## Tech Stack

Backend:
- FastAPI
- SQLAlchemy
- Python

AI:
- Groq API (Llama 3.1)

Frontend:
- HTML
- CSS
- Jinja templates

## Workflow

1. User logs in
2. Uploads questionnaire
3. Uploads reference documents
4. System parses questions
5. AI generates answers using references
6. User reviews and edits answers
7. Export final document

## Assumptions

- Questionnaires contain newline separated questions
- Reference documents are trusted internal sources
- Latest answer version is exported

## Engineering Considerations

Several edge cases were handled during development.

- Missing Reference Evidence
- API Rate Limits
- Invalid API Key Handling
- Review Safety
- Sequential LLM Execution

## Trade-offs

- Simple retrieval instead of vector embeddings
- Heuristic confidence scoring
- Sequential LLM generation

## Improvements With More Time

- Vector based document retrieval
- Async background processing
- Version history for answers
- Partial regeneration per question
- Improved confidence scoring using similarity metrics

## Deployment 

Live application:
```
https://sentinel-secureworks.onrender.com/
```

Important Note:

This application is deployed using Render Free Tier.
The server automatically sleeps after periods of inactivity.
The first request after inactivity may take 20–40 seconds to wake the server.
After waking, the application functions normally.

## ScreenShots

- Landing / Signup page:
  <img width="1918" height="862" alt="image" src="https://github.com/user-attachments/assets/4ac08cf5-47bf-4cdd-9f56-504f2a674fe2" />

- Dashboard (Questionnaires Tab):
  <img width="1918" height="863" alt="image" src="https://github.com/user-attachments/assets/c2dc6be7-0326-4510-9c10-250082622aa7" />

- Dashboard (Upload tab):
  <img width="1918" height="863" alt="image" src="https://github.com/user-attachments/assets/b054e437-066d-40c0-a4e1-e0f8a32695f4" />

- Dashboard (Reference upload tab):
  <img width="1918" height="862" alt="image" src="https://github.com/user-attachments/assets/546d932b-487b-4e03-9226-e1ff6697a1b1" />



## Repository
Github Repository:
https://github.com/LEADisDEAD/Sentinel-SecureWorks


