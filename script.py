import os
from groq import Groq
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont

# Initialize Groq API client
client = Groq(
    api_key="YOUR API KEY",
)

def get_user_input():
    words = input("Enter some words: ")
    theme = input("Enter a theme for the poem: ").strip()
    is_acrostic = input("Do you want an acrostic poem? (yes/no): ").strip()

    while is_acrostic not in ["yes", "no"] : is_acrostic = input("Please enter 'yes' or 'no': ").strip()

    words += f" . Use this phrase and create a poem.Use this theme: {theme} . Just give poem dont add note or explanation"

    if is_acrostic == "yes":  words += f" . Use the first letter of {theme} to create the poem. Make sure to create that many lines using only the letters in the theme once."
    else: words += " . Just 8 lines."

    return words,theme,is_acrostic

# Get user input
words, theme, is_acrostic= get_user_input()
# Generate poem using the API
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": words,
        }
    ],
    model="llama3-8b-8192",
)

def play_poem_audio(poem_text):
    tts = gTTS(text=poem_text, lang="en")
    tts.save("poem_audio.mp3")
    os.system("start poem_audio.mp3")

def visualize_poem(poem_text, theme):
    # Create an image for the poem
    img = Image.new("RGB", (800, 600), "white")
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default()
    draw.text((50, 50), poem_text, fill="black", font=font)

    # Add a rectangle with theme color
    theme_color = {"happiness": "yellow", "sadness": "blue", "love": "pink"}.get(theme, "gray")
    draw.rectangle([50, 500, 750, 550], fill=theme_color)

    # Save the image
    img.save("poem_visual.png")
# Extract and clean the generated poem
poem = chat_completion.choices[0].message.content


poem = poem.split("\n")  # Remove the first line if necessary

while poem[1] and poem[1]=="": poem = poem[2:]

if is_acrostic == "yes":
    for i in range(len(poem)):
        try:
            poem[i] = poem[i].split("-")[1].strip()
        except:
            poem[i] =""
poem = "\n".join(poem)


print("\n--- Your Poem ---\n")
print(poem)
print("\n------\n")

# Visualize and play the poem
visualize_poem(poem, theme)
play_poem_audio(poem_text=poem)

