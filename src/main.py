import openai

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello, I'm John."},
    {"role": "assistant", "content": "Hi John, how can I help you today?"},
    {"role": "user", "content": "Do you know my name?"},
  ]
)

print(response)
