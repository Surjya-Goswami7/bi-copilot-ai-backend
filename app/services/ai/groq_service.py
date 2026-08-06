from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_dataset(df, requirement):

    columns = list(df.columns)

    dtypes = {
        col: str(dtype)
        for col, dtype in df.dtypes.items()
    }

    rows = len(df)

    preview = df.head(20).to_csv(index=False)

    prompt = f"""
You are a Senior Power BI Consultant.

Business Requirement:

{requirement}

Dataset Information

Rows:
{rows}

Columns:
{columns}

Data Types:
{dtypes}

Dataset Preview:

{preview}

Analyze the dataset.

Return ONLY valid JSON.

Use exactly this format:

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

Rules:

- Return ONLY JSON.
- No markdown.
- No explanation.
- No ```json.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content