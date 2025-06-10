import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)

result = client.models.generate_content(model = "gemini-2.0-flash-001", contents ="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")
print(result.text)
print(f"Prompt tokens: {result.usage_metadata.prompt_token_count}")
print(f"Response tokens: {result.usage_metadata.candidates_token_count}")


if len(sys.argv) < 2:
    print("Error:Please enter aprompt")
    sys.exit(1)
prompt = sys.argv[1]
client.models.generate_content(model = "gemini-2.0-flash-001", contents = prompt)