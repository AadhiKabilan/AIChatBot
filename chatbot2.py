import tkinter as tk
from PIL import Image, ImageTk

# Function to create a semi-transparent overlay effect
def create_overlay(canvas, x, y, width, height):
    # Create a rectangle with a white fill and a solid color
    canvas.create_rectangle(x, y, x + width, y + height, fill='#ffffff', outline='')

# Initialize the Tkinter window
root = tk.Tk()
root.title("AI Girlfriend Bot")
root.geometry("400x600")

# Load the background image
bg_image = Image.open("background.png").resize((400, 600), Image.LANCZOS)
bg_image_tk = ImageTk.PhotoImage(bg_image)

# Create a canvas to hold the background image
canvas = tk.Canvas(root, width=400, height=600)
canvas.pack(fill="both", expand=True)

# Add the background image to the canvas
canvas.create_image(0, 0, anchor="nw", image=bg_image_tk)

# Create a semi-transparent overlay effect
create_overlay(canvas, 25, 100, 350, 300)  # White rectangle as overlay

# Create a frame on top of the overlay
frame = tk.Frame(canvas, bg='lightgray', bd=0)
frame.place(relx=0.5, rely=0.5, anchor='center', width=350, height=300)

# Create the text box
chat_window = tk.Text(frame, bg='lightgray', font=("Arial", 12), wrap='word', height=15, bd=0)
chat_window.pack(expand=True, fill='both', padx=10, pady=10)

# Example for sending messages
def send():
    user_input = "User message"  # Replace with user input
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"You: {user_input}\n")
    chat_window.config(state=tk.DISABLED)

# Sample button to demonstrate functionality
send_button = tk.Button(root, text="Send", command=send)
send_button.pack(pady=20)

# Start the GUI loop
root.mainloop()
