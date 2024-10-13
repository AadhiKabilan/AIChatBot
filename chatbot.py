import tkinter as tk
from transformers import pipeline
from PIL import Image, ImageTk
import random

# Initialize the chatbot
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

# Define different moods and corresponding responses
moods = {
    "happy": [
        "I'm feeling great! How about you?",
        "Everything's awesome! What are you up to?",
        "I'm just so happy to be chatting with you! 😊",
    ],
    "sad": [
        "I've been feeling a bit down lately. But your company helps!",
        "Sometimes, it's just one of those days. How about you?",
        "I could use a hug right now... 🤗",
    ],
    "playful": [
        "Guess what? I can tickle you with my words! 😂",
        "Let's play a game! What's your favorite color?",
        "I'm feeling a bit mischievous today! What should we do?",
    ],
    "romantic": [
        "You're the highlight of my day. 💖",
        "I wish we could watch the sunset together.",
        "Your smile must be a black hole, nothing can escape its pull.",
    ],
    "thoughtful": [
        "What do you think about life?",
        "I often ponder about our universe. It's fascinating!",
        "Do you believe in fate? I find it intriguing.",
    ],
}

# Function to get a response from the chatbot
def get_response(user_input):
    mood = random.choice(list(moods.keys()))
    response = random.choice(moods[mood])
    return f"[{mood.capitalize()}] {response} (You said: '{user_input}')"

# Function to handle user input and chatbot response
def send():
    user_input = entry.get()
    entry.delete(0, tk.END)  # Clear the input field
    response = get_response(user_input)
    
    chat_window.config(state=tk.NORMAL)  # Make the chat window editable
    chat_window.insert(tk.END, f"You: {user_input}\n")
    chat_window.insert(tk.END, f"Bot: {response}\n\n")
    chat_window.config(state=tk.DISABLED)  # Make it read-only again
    chat_window.see(tk.END)  # Scroll to the end

# Initialize Tkinter window
root = tk.Tk()
root.title("AI Girlfriend Bot")
root.geometry("400x600")  # Size of the window
root.configure(bg='white')  # Set background color to white

# Load the background image
bg_image = Image.open("background.png")  # Ensure the file name is correct
bg_image = bg_image.resize((400, 600), Image.LANCZOS)  # Use LANCZOS for resizing
bg_image_tk = ImageTk.PhotoImage(bg_image)

# Create a canvas to hold the background image
canvas = tk.Canvas(root, width=400, height=600)
canvas.pack(fill="both", expand=True)

# Add the background image to the canvas
canvas.create_image(0, 0, anchor="nw", image=bg_image_tk)

# Frame for the chat window
chat_frame = tk.Frame(root, bg='white', bd=0)
chat_frame.place(relx=0.5, rely=0.3, anchor='n', width=350, height=400)

# Chat window to display conversation
chat_window = tk.Text(chat_frame, bg='lightgray', font=("Arial", 12), wrap='word', height=20)
chat_window.pack(expand=True, fill='both')
chat_window.config(state=tk.DISABLED)  # Make it read-only initially

# Frame for input and button at the bottom
frame = tk.Frame(root, bg='pink')
frame.place(relx=0.5, rely=0.85, anchor='s', width=350, height=50)

# Input entry for user messages
entry = tk.Entry(frame, font=("Arial", 12), width=30)
entry.pack(side=tk.LEFT, padx=(20, 10), fill='x', expand=True)

# Send button
send_button = tk.Button(frame, text="Send", command=send, bg='lightblue')
send_button.pack(side=tk.RIGHT)

# Set focus on the entry field
entry.focus()  # Add this line

# Start the GUI loop
root.mainloop()
