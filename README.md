# Sentinel SecureWorks

AI-powered security questionnaire automation tool that generates grounded answers using internal reference documentation.

## Industry

Cybersecurity / SaaS Compliance Automation

## Fictional Company

Sentinel SecureWorks is a fictional cybersecurity SaaS company that provides enterprise grade security infrastructure monitoring and compliance automation tools. The platform helps organizations maintain security posture, automate compliance workflows, and respond efficiently to vendor security questionnaires.

## Problem

Security questionnaires and vendor risk assessments are time consuming and repetitive. Teams must manually locate answers across multiple internal documents.

This tool automates that process by:

1. Parsing questionnaires
2. Retrieving relevant reference information
3. Generating grounded answers with citations
4. Allowing human review and editing
5. Exporting a structured response document

## Features

- User authentication
- Questionnaire upload
- Reference document upload
- AI-generated answers
- Citation grounding
- Confidence scoring
- Review & edit workflow
- Structured DOCX export

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
