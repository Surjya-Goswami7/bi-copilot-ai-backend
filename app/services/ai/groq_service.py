from groq import Groq
from dotenv import load_dotenv
import os
import json

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
      "dax_measures":[
        {{
            "measure_name":"",
            "dax_formula":"",
            "description":""
        }}
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

DAX Rules:

- Generate DAX measures based on the dataset and business requirement.
- Do not assume the dataset is a Sales dataset.
- Generate measures appropriate for the identified dataset type.
- Generate MTD or YTD measures only when a suitable date column exists and time-based analysis is relevant.
- For HR datasets, generate relevant HR measures when supported by the data.
- For Inventory datasets, generate relevant inventory measures when supported by the data.
- For Sales datasets, generate relevant sales measures when supported by the data.
- Use only columns that actually exist in the dataset.
- Never invent column names.
- DAX formulas must use valid Power BI DAX syntax.
- Do not generate a DAX measure if the required column does not exist.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content

    return json.loads(content)