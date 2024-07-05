# Pyshorteners used to shorten the URLs.
import pyshorteners
# Pyperclip used for copying and pasting text to the clipboard
import pyperclip
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

# Create the main application window
win = tk.Tk()
win.title("URL Shortener Application")
win.geometry("650x300")
win.configure(bg="#18252D")

def short():
    try:
        # Get the URL from the entry widget
        url = original_url.get()
        # Initialize the URL shortener
        shortener = pyshorteners.Shortener()
        # Shorten the URL
        shorted_url = shortener.tinyurl.short(url)
        # Show the shortened URL in the shortened entry
        shortened_url.insert(0, shorted_url)
    except:
        # Handle any exceptions that occur
        showerror("Error", "Please! Enter Url:")

def copyurl():
    urlshort = shortened_url.get()
    pyperclip.copy(urlshort)

label1 = tk.Label(win, text=" URL Shortener", font="impact 16")
label1.grid(row=0,column=1, pady=10)

# Create and place widgets using grid
url_label = tk.Label(win, text="Enter URL Here:", font="impact 14", bg="white", fg="black")
url_label.grid(row=1, column=0, padx=20, pady=20, sticky=tk.W)

original_url = tk.Entry(win, font="impact 14", bg="white", width=40, bd=8)
original_url.grid(row=1, column=1, padx=10, pady=10)

button1 = ttk.Button(win, text="Shorten URL", command=short)
button1.grid(row=2, column=1, columnspan=1, pady=20)

shortener_label = tk.Label(win, text="Shortened URL:", font="impact 14", bg="white", fg="black")
shortener_label.grid(row=3, column=0, padx=10, pady=10)

Shortened_url = tk.StringVar()
shortened_url = tk.Entry(win, font="impact 14", bg="white", width=40, bd=8)
shortened_url.grid(row=3, column=1, padx=10, pady=10)

button2 = ttk.Button(win,text="Copy Shortened Url", command=copyurl)
button2.grid(row=4,column=1, columnspan=1, pady=20)

# Start the main event loop
win.mainloop()
