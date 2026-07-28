from fastapi import APIRouter, UploadFile, File, Form
import os

from app.services.ingestion.factory_ingestor import IngestionFactory
from app.services.profiler import DatasetProfiler
from app.services.ai.groq_service import ask_groq

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    requirement: str = Form(...)
):

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(filepath, "wb") as buffer:
        buffer.write(await file.read())

    df = IngestionFactory.read(filepath)

    profile = DatasetProfiler.profile(df)

    columns = list(df.columns)

    dtypes = {
        col: str(dtype)
        for col, dtype in df.dtypes.items()
    }

    preview = df.head(20).to_csv(index=False)

    prompt = f"""
You are an expert Power BI Consultant.

Business Requirement:

{requirement}


Dataset Preview:
{preview}

Your job is to understand the dataset and suggest a Power BI dashboard.

Return ONLY valid JSON.

Use this exact format.

{{
    "dataset_type":"",
    "business_understanding":"",
    "kpis":[
        ""
    ],
    "dimensions":[
        ""
    ],
    "measures":[
        ""
    ],
    "charts":[
        {{
            "title":"",
            "chart_type":"",
            "x_axis":"",
            "y_axis":"",
            "reason":""
        }}
    ]
}}

Do not explain anything.

Do not use markdown.

Do not write ```json.

Return only JSON.
"""

    ai_response = ask_groq(prompt)

    return {
        "filename": file.filename,
        "profile": profile,
        "ai_analysis": ai_response
    }