import json
import fitz  # PyMuPDF
import os
import datetime
from collections import defaultdict

with open('challenge1b_input.json', 'r') as f:
    config = json.load(f)

documents = config["documents"]
persona = config["persona"]["role"]
job = config["job_to_be_done"]["task"]

results = {
    "metadata": {
        "input_documents": [doc["filename"] for doc in documents],
        "persona": persona,
        "job_to_be_done": job,
        "processing_timestamp": datetime.datetime.now().isoformat()
    },
    "extracted_sections": [],
    "subsection_analysis": []
}

keywords = job.lower().split() + persona.lower().split()

def score(text):
    return sum(1 for k in keywords if k in text.lower())

section_id = 0

for doc in documents:
    file_path = os.path.join("PDFs", doc["filename"])
    doc_title = doc["title"]
    pdf = fitz.open(file_path)

    section_scores = []
    for page_num in range(len(pdf)):
        page = pdf.load_page(page_num)
        text = page.get_text()

        relevance = score(text)
        if relevance > 2:  
            section_scores.append((relevance, page_num + 1, text.strip()))

    section_scores.sort(reverse=True)  

    for rank, (relevance, pg, text) in enumerate(section_scores[:3], start=1):
        title = text.split("\n")[0][:50]  
        results["extracted_sections"].append({
            "document": doc["filename"],
            "section_title": title,
            "importance_rank": rank,
            "page_number": pg
        })

        results["subsection_analysis"].append({
            "document": doc["filename"],
            "refined_text": text[:500],  
            "page_number": pg
        })

with open("challenge1b_output.json", "w") as out:
    json.dump(results, out, indent=2)
