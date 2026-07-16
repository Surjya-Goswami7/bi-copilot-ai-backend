import os

from app.services.ingestion.csv_ingestor import read_csv_file
from app.services.ingestion.excel_ingestor import read_excel_file
from app.services.ingestion.pdf_ingestor import read_pdf_file


class IngestionFactory:

    @staticmethod
    def read(filepath: str):

        extension = os.path.splitext(filepath)[1].lower()

        if extension == ".csv":
            return read_csv_file(filepath)

        elif extension in [".xlsx", ".xls"]:
            return read_excel_file(filepath)

        elif extension == ".pdf":
            return read_pdf_file(filepath)

        else:
            raise ValueError(f"Unsupported file type: {extension}")