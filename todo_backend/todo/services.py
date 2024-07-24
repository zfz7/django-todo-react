import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY
client = openai.OpenAI()

def generate_text(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are to summarize the contents of the following tasks."},
            {"role": "user", "content": "The tasks are: " + prompt}
        ]
    )   
    return response.choices[0].text.strip()