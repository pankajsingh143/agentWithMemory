import os
from ollama import Client

messages = [
    {
        "role": "system",
        "content": "You are a helpful AI Research assistant."
    }
]

client = Client(
    host="https://ollama.com",
    headers={"Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}"}
)

while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting the chat. Goodbye!")
        break
    messages.append({
        "role": "user",
        "content": user_input,
    })
    response = client.chat(
        model="gpt-oss:20b",
        messages=messages)
    assistant_reply = response['message']['content']
    print(f"Assistant: {assistant_reply}")
    messages.append({
        "role": "assistant",
        "content": assistant_reply,
    })  