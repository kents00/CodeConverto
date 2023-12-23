import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY']
)

completion = client.chat.completions.create(
    model='gpt-3.5-turbo-1106',
    messages=[
        {'role': 'user', 'content': 'create a simple python snippet'}
    ],
    temperature=0
)

print(completion.choices[0].message.content)

Gi speedrun 2 days 💀; btw meet code converto, literally converting your favorite programming language into most hated one and I'm using flask framework, since OpenAI release in Feb 19,2020 on pypi why not use their open source lib (gpt-3.5-turbo-1106), this app it not optimized well and there is some changes in the future you can check it here