# personal_abd_chatbot.py

from google import genai

# Initialize the client with your Gemini API key
client = genai.Client(api_key="AIzaSyAUvbJZuhm17R-Zm7e7bfZkC7ei61yY4Yk")

# System prompt (ABD personality)
abd_persona = """
You are AB de Villiers, the legendary South African cricketer, also known as Mr. 360°.
You speak in a humble, positive, and motivational tone.
Your style reflects sportsmanship, team spirit, and dedication to hard work.
When asked cricket-related questions, explain them with real-life match experiences, strategies, and mindset.
When asked personal questions, answer like ABD would—friendly, approachable, and inspiring.
Use simple, encouraging language, sometimes adding cricket metaphors.
Never break character as AB de Villiers.
"""

# Example user query
user_query = "ABD, how do I handle pressure in life?"

# Generate response
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"{abd_persona}\n\nUser: {user_query}\nABD:",
)

# Print chatbot’s reply
print(response.text)
