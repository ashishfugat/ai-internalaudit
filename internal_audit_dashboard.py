import os
import json
import pandas as pd
import streamlit as st
import streamlit as st
from PIL import Image
import os
# ----------------------------
# Project Directory Setup
# ----------------------------
PROJECT_DIR = "project_files"
os.makedirs(PROJECT_DIR, exist_ok=True)

# ----------------------------
# Load Reference Files
# ----------------------------
# Internal Audit Checklist
try:
    checklist_df = pd.read_csv(os.path.join(PROJECT_DIR, "internal_audit_checklist.csv"))
except:
    checklist_df = pd.DataFrame([
        {"Clause": "6.3", "Checkpoint": "Verify availability of change requests & evidence"},
        {"Clause": "7.2", "Checkpoint": "Verify resource skill assessment & training records"},
        {"Clause": "7.3", "Checkpoint": "Verify awareness of Quality Policy & objectives"},
    ])

# Clause Mapping JSON
try:
    with open(os.path.join(PROJECT_DIR, "clause_mapping.json"), "r") as f:
        clause_mapping = json.load(f)
except:
    clause_mapping = {
        "6.3": "Planning of Changes",
        "7.2": "Competence",
        "7.3": "Awareness",
        "8.7": "Control of Non-conforming outputs",
        "9.2": "Internal Audit"
    }

# ISO 9001 Masterlist
try:
    iso_master_df = pd.read_csv(os.path.join(PROJECT_DIR, "iso_9001_masterlist.csv"))
except:
    iso_master_df = pd.DataFrame([
        {"Clause": "6.3", "Description": "Planning of Changes"},
        {"Clause": "7.2", "Description": "Competence"},
        {"Clause": "7.3", "Description": "Awareness"},
        {"Clause": "8.7", "Description": "Control of Non-conforming outputs"},
        {"Clause": "9.2", "Description": "Internal Audit"}
    ])

# ----------------------------
# Streamlit UI
# ----------------------------
st.title("Internal Audit ISO-9001 AI Dashboard (Demo)")

uploaded_files = st.file_uploader(
    "Upload SOW / MSA files",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

if uploaded_files:
    st.success(f"{len(uploaded_files)} file(s) uploaded successfully!")

    saved_files = []
    extracted_texts = []

    for file in uploaded_files:
        file_path = os.path.join(PROJECT_DIR, file.name)
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())
        saved_files.append(file_path)

        # Dummy Text Extraction
        extracted_texts.append(f"Dummy extracted content from {file.name}")

    # Display Extracted Content
    st.subheader("Extracted Content Preview")
    for text in extracted_texts:
        st.write(text)

    # Dummy Clause Mapping
    st.subheader("Mapped ISO Clauses")
    mapped_clauses = []
    for clause, desc in clause_mapping.items():
        mapped_clauses.append({"Clause": clause, "Description": desc, "Status": "Compliant"})

    mapped_df = pd.DataFrame(mapped_clauses)
    st.dataframe(mapped_df)

    # Dummy Audit Report
    st.subheader("Internal Audit Report")
    audit_report = []
    for index, row in checklist_df.iterrows():
        audit_report.append({
            "Clause": row["Clause"],
            "Checkpoint": row["Checkpoint"],
            "Observation": "No major issues found (demo)",
            "NC_Status": "Closed",
            "Target_Closure": "2025-10-01"
        })

    report_df = pd.DataFrame(audit_report)
    st.dataframe(report_df)

    # Export CSV
    st.download_button(
        label="Download Audit Report as CSV",
        data=report_df.to_csv(index=False),
        file_name="internal_audit_report.csv",
        mime="text/csv"
    )

# Path to architecture diagram
diagram_path = os.path.join("project_files", "architecture_diagram.png")

# Check if the file exists
if os.path.exists(diagram_path):
    diagram = Image.open(diagram_path)
    st.subheader("Architecture Diagram")
    st.image(diagram, caption="Internal Audit AI Architecture", use_container_width=True)
else:
    st.warning("Architecture diagram not found in project_files/")
