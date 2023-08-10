from tkinter import *
from tkinter import filedialog
from cryptography.fernet import Fernet
import mimetypes

# Generate a new key
new_key = Fernet.generate_key()
new_keyfernet = Fernet(new_key)

# For encryption
def encryptt():
    filepath = filedialog.askopenfilename()

    if filepath:
        with open(filepath, 'rb') as f:
            contents = f.read()
        encrypted = new_keyfernet.encrypt(contents)

        with open(f'{filepath}.encrypt', 'wb') as f:
            f.write(encrypted)

        result.config(text=f"Encryption Successful. Please check filepath \n{filepath}.encrypt", fg="green")

# For decryption
def decryptt():
    filepath = filedialog.askopenfilename()

    if filepath:
        with open(filepath, 'rb') as f:
            contents = f.read()
        decrypted = new_keyfernet.decrypt(contents)

        filepath = filepath.split('.encrypt')

        with open(filepath[0], 'wb') as f:
            f.write(decrypted)

        result.config(text=f"Decryption Successful. Please check filepath \n{filepath[0]}", fg="green")

# Function to create a new text file
def create_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    
    if filepath:
        with open(filepath, 'w') as f:
            f.write("Hello, this is a new text file!")
        
        result.config(text=f"File created successfully: {filepath}", fg="green")

# Function to get and display the file type
def get_file_type():
    filepath = filedialog.askopenfilename()

    if filepath:
        file_type, _ = mimetypes.guess_type(filepath)
        result.config(text=f"Selected file type: {file_type}", fg="blue")

# GUI for encryption, decryption, file creation, and file type
root = Tk()
root.geometry("1000x550+100+50")  # screen size
root.title("Shugam Python enc/dec tool")

# Styling
root.configure(bg="#f0f0f0")  # Set background color

title = Label(root, text="File Encryptor/Decryptor/File Creator/File Type Checker", font=("Calibri", 28, "bold"), fg="#333", bg="#f0f0f0")
title.pack(pady=20)

frame = Frame(root, bg="#f0f0f0")
frame.pack(pady=20)

# For encrypt
encrypt = Button(frame, text="Encrypt", width=15, font=("Calibri", 20), bg="#66c2ff", fg="white", command=encryptt)
encrypt.pack(pady=10)

# For decrypt
decrypt = Button(frame, text="Decrypt", width=15, font=("Calibri", 20), bg="#ff6666", fg="white", command=decryptt)
decrypt.pack(pady=20)

# For file creation
create = Button(frame, text="Create File", width=15, font=("Calibri", 20), bg="#66ff66", fg="white", command=create_file)
create.pack(pady=10)

# For file type
get_type = Button(frame, text="Get File Type", width=15, font=("Calibri", 20), bg="#ffcc00", fg="white", command=get_file_type)
get_type.pack(pady=10)

# Result label
result = Label(frame, font=('Calibri', 20), bg="#f0f0f0", height=4, wraplength=800)
result.pack(pady=20)

# Program exit
Exit = Button(frame, text="Exit", font=("Calibri", 20), padx=10, fg='white', bg='#666', command=root.destroy)
Exit.pack()

root.mainloop()
