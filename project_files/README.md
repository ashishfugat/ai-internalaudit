Internal Audit AI Dashboard (Demo)
Overview

The Internal Audit AI Dashboard is a Streamlit-based demo simulating an automated internal audit workflow.
It allows users to:

Upload SOW/MSA files

Extract content (dummy AI/OCR)

Map content to ISO 9001 clauses

Compare with an internal audit checklist

Generate a professional audit report

Download the report as CSV

This demo is intended to showcase workflow automation for internal audits. In a production version, AI/OCR tools would replace the dummy extraction.

Project Structure
internal_audit_demo/
│
├── project_files/
│   ├── internal_audit_checklist.csv     # Internal audit checklist
│   ├── clause_mapping.json              # ISO clause mapping
│   └── iso_9001_masterlist.csv          # ISO 9001 master clauses
│
├── internal_audit_dashboard.py          # Main Streamlit app
└── requirements.txt                     # Python dependencies

Installation

Clone or unzip the project folder:

git clone <repo-url>
# or unzip internal_audit_demo.zip
cd internal_audit_demo


Install dependencies:

pip install -r requirements.txt

Running the Dashboard
streamlit run internal_audit_dashboard.py


Open the browser link provided (usually http://localhost:8501).

Dashboard Layout
1️⃣ Upload SOW/MSA Files

Upload your project documents (PDF/DOCX) which are stored in the project_files folder.

2️⃣ Extracted Content Preview

The dashboard displays dummy extracted content for each uploaded file.

3️⃣ ISO Clause Mapping

Mapped ISO 9001 clauses are displayed with compliance status.

4️⃣ Internal Audit Report

Audit report compares checklist items with project documents and shows observations, NC status, and target closure.

5️⃣ Export Audit Report

Download the audit report as a CSV file for sharing or record-keeping.

Reference Files

internal_audit_checklist.csv – Checkpoints for internal audit

clause_mapping.json – Maps audit points to ISO 9001 clauses

iso_9001_masterlist.csv – Master list of ISO 9001 clauses

Notes

This is a demo version with dummy AI/OCR processing.

Real implementation can use AWS Textract, Azure Form Recognizer, or AI embeddings for automated text extraction.

NCs and missing evidence can be highlighted automatically in future versions.

Architecture Overview
Frontend (ReactJS) → Hosted on Azure Static Web Apps

Backend (Azure Functions – .NET 8) → Orchestrates workflow

Storage → Azure Blob Storage (store uploaded .txt SOW docs + reports)

AI Services → Azure OpenAI (embeddings + GPT for Q&A)

Vector DB → Azure Cognitive Search (vector search enabled)

Reporting → Azure Functions with Pandas/ReportLab (Excel/PDF generation)

