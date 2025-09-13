Internal Audit AI Dashboard (Demo)
Overview
 
<img width="1536" height="1024" alt="architecture_diagram" src="https://github.com/user-attachments/assets/7bf27125-2190-4c71-b539-b74242b2453e" />

The Internal Audit AI Dashboard is a Streamlit-based demo simulating an automated internal audit workflow.
It allows users to:

Upload SOW/MSA files

Extract content (dummy AI/OCR)

Map content to ISO 9001 clauses

Compare with an internal audit checklist

Generate a professional audit report

Download the report as CSV

This demo is intended to showcase workflow automation for internal audits. In a production version, AI/OCR tools would replace the dummy extraction.

Architecture Diagram

The dashboard follows this architecture for internal audit automation:

Project Files (SOW/MSA)
          │
          ▼
  File Upload via Streamlit
          │
          ▼
  Text Extraction (Dummy AI/OCR)
          │
          ▼
  Clause Mapping (ISO 9001)
          │
          ▼
  Checklist Comparison & Audit Report
          │
          ▼
Dashboard Output + CSV Export


You can display your actual architecture diagram uploaded under the project directory using Streamlit:

from PIL import Image
import os
import streamlit as st

diagram_path = os.path.join("project_files", "architecture_diagram.png")
if os.path.exists(diagram_path):
    diagram = Image.open(diagram_path)
    st.subheader("Architecture Diagram")
    st.image(diagram, caption="Internal Audit AI Architecture", use_column_width=True)
else:
    st.warning("Architecture diagram not found in project_files/")


Place your uploaded architecture diagram in project_files/architecture_diagram.png to render it on the dashboard.

Dashboard Layout
1️⃣ Upload SOW/MSA Files

Upload your project documents (PDF/DOCX) which are stored in the project_files/ folder.

2️⃣ Extracted Content Preview

Displays dummy extracted content for each uploaded file.

3️⃣ ISO Clause Mapping

Mapped ISO 9001 clauses are displayed with compliance status.

4️⃣ Internal Audit Report

Audit report shows observations, NC status, and target closure.

5️⃣ Export Audit Report

Download the audit report as a CSV file.

Project Structure
internal_audit_demo/
│
├── project_files/
│   ├── internal_audit_checklist.csv
│   ├── clause_mapping.json
│   ├── iso_9001_masterlist.csv
│   └── architecture_diagram.png    # Uploaded architecture diagram
│
├── internal_audit_dashboard.py
└── requirements.txt

Usage

Upload SOW/MSA files → stored in project_files/.

View extracted content, mapped ISO clauses, and audit report.

Download CSV report for stakeholders.

The architecture diagram illustrates the workflow.

Notes

This is a demo version with dummy AI/OCR processing.

Real implementation can use AWS Textract, Azure Form Recognizer, or AI embeddings for automated text extraction.

NCs and missing evidence can be highlighted automatically in future versions.
