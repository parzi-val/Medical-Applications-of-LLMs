import tkinter as tk
import google.generativeai as genai
import textwrap

api = "AIzaSyBeV7CdcxwBO588Xhb3FTgxjaZSzTQ6Q98"

genai.configure(api_key=api)
model = genai.GenerativeModel('gemini-1.0-pro')

def process_input():
    input_text = input_field.get()
    input_text += "(In 4 - 5 lines)"
    response = model.generate_content(input_text).candidates[0].content.parts[0].text
    response = textwrap.fill(response,width = 50)

    display_text.config(state=tk.NORMAL)
    display_text.delete(1.0, tk.END) 
    display_text.insert(tk.END, response+ '\n')
    display_text.config(state=tk.DISABLED)
    input_field.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Diabetes Chatbot")

# Create input field
input_field = tk.Entry(root, width=50)
input_field.grid(row=1, column=0, padx=5, pady=10)

# Create send button
send_button = tk.Button(root, text="Send", command=process_input)
send_button.grid(row=1, column=1, padx=5, pady=10)

# Create display text area
display_text = tk.Text(root, height=20, width=50)
display_text.grid(row=0, column=0, columnspan=2)

# Run the Tkinter event loop
root.mainloop()
