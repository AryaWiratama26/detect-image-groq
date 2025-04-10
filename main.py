from groq import Groq
import os
from dotenv import load_dotenv
import markdown

load_dotenv()
API_KEY = os.getenv('API_KEY')

client = Groq(api_key=API_KEY)
completion = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Kerjakan soal ini"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://pict.sindonews.net/webp/480/pena/news/2023/03/19/46/1050763/tidak-semudah-itu-ferguso-soal-matematika-ini-sukses-bikin-pusing-netizen-tro.webp"
                    }
                }
            ]
        }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)

answer_bot = completion.choices[0].message.content
print(answer_bot)

with open('index.html', 'w', encoding='utf-8') as file:
    file.write(markdown.markdown(answer_bot))
    