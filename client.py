from openai import OpenAI
client = OpenAI(
    api_key=  "api key xyz"
)

response = client.responses.create(
    model="gpt-5.5",
    input="what is coding."
)

print(response.output_text)