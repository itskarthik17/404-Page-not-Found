'''
Folder Structure need to be like this
📁 PDFs/
├─ doc1.pdf
├─ doc2.pdf
📄 challenge1b_input.json
📄 main.py
'''

# Approach Explanation

## Overview

This system is designed to process a collection of PDFs and extract the most relevant content based on a given persona and their job-to-be-done. It produces structured JSON output with ranked sections and refined summaries for efficient information retrieval.

## Methodology

1. **Input Parsing:**
   The system reads the input JSON file containing the persona, task, and list of documents to be analyzed.

2. **PDF Processing:**
   Using PyMuPDF, each PDF is parsed page by page to extract text content. This is efficient and suitable for CPU-only constraints.

3. **Relevance Scoring:**
   A simple keyword-based scoring function counts how many words from the persona and task appear on each page. Pages with higher matches are considered more relevant.

4. **Section Ranking and Title Extraction:**
   Pages with a score above a threshold are sorted and the top 3 are selected. The first line of text from each is used as a pseudo section title.

5. **Subsection Analysis:**
   A snippet of up to 500 characters is extracted from each selected page to serve as a quick refined summary.

6. **Output Generation:**
   The results are compiled into a JSON file, including metadata, top sections, and subsection analyses.

## Performance

- Runs on CPU
- Uses less than 1GB memory
- Processes 3-5 documents in under 60 seconds

This approach ensures simplicity, performance, and relevance without needing internet or large models.
