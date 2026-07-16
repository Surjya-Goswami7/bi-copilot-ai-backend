import pdfplumber
import pandas as pd


def read_pdf_file(filepath: str):

    rows = []

    with pdfplumber.open(filepath) as pdf:

        for page in pdf.pages:

            table = page.extract_table()

            if table:
                rows.extend(table)

    return pd.DataFrame(rows)