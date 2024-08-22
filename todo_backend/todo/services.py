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
    return response.choices[0].message.content.strip()


def translate(text, language):
    response = client.chat.completions.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": f"You are a translator that translates text into {language}."},
            {"role": "user", "content": text}
        ],
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7
    )

    return response.choices[0].message.content.strip()
