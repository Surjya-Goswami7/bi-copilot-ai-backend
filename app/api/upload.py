from fastapi import APIRouter, UploadFile, File
import os
from app.services.ingestion.factory_ingestor import IngestionFactory
from app.services.profiler import DatasetProfiler
from app.services.analyzer import DatasetAnalyzer

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(filepath, "wb") as buffer:
        buffer.write(await file.read())

    df = IngestionFactory.read(filepath)

    profile = DatasetProfiler.profile(df)

    analysis = DatasetAnalyzer.analyze(df)

    return {
    "filename": file.filename,
    "profile": profile,
    "analysis": analysis
}