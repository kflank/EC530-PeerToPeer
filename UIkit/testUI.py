import tkinter as tk
import p2p
# Create the main window
root = tk.Tk()

# Create a label and input field
label = tk.Label(root, text="Enter your name:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Create a function to handle the submit button
def submit_name():
    name = entry.get()
    print("Hello,", name)

# Create a submit button
button = tk.Button(root, text="Submit", command=submit_name)
button.pack()

# Start the main event loop
root.mainloop()
