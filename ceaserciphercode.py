import tkinter as tk
from tkinter import messagebox

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text


def perform_action():
    # Get input from user
    message = entry_message.get()
    shift = entry_shift.get()
    
    # Check if the shift is an integer
    try:
        shift = int(shift)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")
        return
    
    # Perform encryption or decryption
    if var_choice.get() == "Encrypt":
        result = encrypt(message, shift)
    elif var_choice.get() == "Decrypt":
        result = decrypt(message, shift)
    
    # Show the result in a message box
    messagebox.showinfo("Result", f"Result: {result}")

# Main window
window = tk.Tk()
window.title("Caesar Cipher")

# Title label
label_title = tk.Label(window, text="Caesar Cipher Encryption/Decryption", font=("Arial", 16))
label_title.pack(pady=10)

# Message input
label_message = tk.Label(window, text="Enter Message:")
label_message.pack()

entry_message = tk.Entry(window, width=50)
entry_message.pack(pady=5)

# Shift value input
label_shift = tk.Label(window, text="Enter Shift Value:")
label_shift.pack()

entry_shift = tk.Entry(window, width=10)
entry_shift.pack(pady=5)

# Encrypt or Decrypt option
var_choice = tk.StringVar(value="Encrypt")  # Default choice is Encrypt

frame_radio = tk.Frame(window)
frame_radio.pack(pady=10)

radio_encrypt = tk.Radiobutton(frame_radio, text="Encrypt", variable=var_choice, value="Encrypt")
radio_encrypt.pack(side="left")

radio_decrypt = tk.Radiobutton(frame_radio, text="Decrypt", variable=var_choice, value="Decrypt")
radio_decrypt.pack(side="right")

# Button to perform action
button_action = tk.Button(window, text="Perform Action", command=perform_action)
button_action.pack(pady=20)

# Run the window loop
window.mainloop()
