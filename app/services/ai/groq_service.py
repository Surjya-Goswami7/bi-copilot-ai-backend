from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_dataset(data_preview: str):

    prompt = f"""
You are an expert Power BI Consultant.

Analyze the following dataset preview and return:

1. Dataset Type
2. Business Understanding
3. KPIs
4. Charts
5. Dimensions
6. Measures

Dataset Preview:

{data_preview}
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