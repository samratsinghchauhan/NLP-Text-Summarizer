import tkinter as tk
from tkinter import scrolledtext, messagebox
from summarizer import summarize_text

def summarize_action():
    input_text = text_input.get("1.0", tk.END).strip()
    if not input_text or len(input_text) < 10:
        messagebox.showwarning("⚠️ Warning", "Please enter at least 10 characters of text.")
        return
    try:
        summary = summarize_text(input_text, num_sentences=3)
        
        # Clear input box
        text_input.delete("1.0", tk.END)

        # Display summary in output box
        text_output.config(state=tk.NORMAL)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, summary)
        text_output.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("❌ Error", f"Something went wrong:\n{str(e)}")

# --- GUI Setup ---
app = tk.Tk()
app.title("🧠 AI Text Summarizer")
app.geometry("900x700")
app.configure(bg="#f8f9fa")

# Fonts and colors
FONT_HEADING = ("Segoe UI", 18, "bold")
FONT_LABEL = ("Segoe UI", 12)
FONT_TEXT = ("Consolas", 12)
BTN_COLOR = "#0077cc"
BTN_HOVER = "#005fa3"

# --- Heading ---
heading = tk.Label(app, text="📝 AI Text Summarizer Tool", font=FONT_HEADING, bg="#f8f9fa", fg="#333")
heading.pack(pady=(20, 10))

# --- Input Section ---
input_label = tk.Label(app, text="Enter text to summarize:", font=FONT_LABEL, bg="#f8f9fa", anchor="w")
input_label.pack(padx=30, anchor="w")

text_input = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=100, height=15, font=FONT_TEXT, bg="#ffffff", bd=1, relief=tk.SOLID)
text_input.pack(padx=30, pady=(5, 20))

# --- Button with hover effect ---
def on_enter(e): summarize_btn.config(bg=BTN_HOVER)
def on_leave(e): summarize_btn.config(bg=BTN_COLOR)

summarize_btn = tk.Button(app, text="🔍 Summarize Text", font=("Segoe UI", 12, "bold"),
                          bg=BTN_COLOR, fg="white", padx=20, pady=10,
                          relief=tk.FLAT, command=summarize_action, cursor="hand2")
summarize_btn.bind("<Enter>", on_enter)
summarize_btn.bind("<Leave>", on_leave)
summarize_btn.pack(pady=10)

# --- Output Section ---
output_label = tk.Label(app, text="Summary:", font=FONT_LABEL, bg="#f8f9fa", anchor="w")
output_label.pack(padx=30, pady=(20, 0), anchor="w")

text_output = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=100, height=10, font=FONT_TEXT, bg="#f1f3f4", bd=1, relief=tk.SOLID)
text_output.config(state=tk.DISABLED)
text_output.pack(padx=30, pady=(5, 30))

# --- Run App ---
app.mainloop()
