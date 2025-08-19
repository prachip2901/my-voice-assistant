from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)