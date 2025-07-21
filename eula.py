import tkinter as tk
from main import CommandProcessor

class AssistantGUI:
    def __init__(self, root):
        self.processor = CommandProcessor()
        root.title("Eula Chat")
        root.geometry("400x300")
        root.configure(bg="white")
        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=0)
        root.columnconfigure(0, weight=1)

        self.text_area = tk.Text(root, wrap=tk.WORD, font=("Consolas", 12), bg="white", fg="black")
        self.text_area.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 0))
        self.text_area.tag_configure("user", justify='right', foreground="blue")
        self.text_area.tag_configure("eula", justify='left', foreground="black")

        input_frame = tk.Frame(root, bg="white")
        input_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
        input_frame.columnconfigure(0, weight=1)

        self.entry = tk.Entry(input_frame, font=("Consolas", 12), bg="white", fg="black")
        self.entry.grid(row=0, column=0, sticky="ew", padx=(0, 10))
        self.entry.bind("<Return>", self.process_input)
        tk.Button(input_frame, text="Gửi", font=("Consolas", 12), command=self.process_input, bg="white").grid(row=0, column=1)

        self.add_eula_message("Chào mừng bạn!")

    def _add_message(self, message, tag):
        self.text_area.config(state='normal')
        self.text_area.insert(tk.END, f"{message}\n", tag)
        self.text_area.config(state='disabled')
        self.text_area.see(tk.END)

    def add_user_message(self, message): self._add_message(message, "user")
    def add_eula_message(self, message): self._add_message(message, "eula")

    def process_input(self, event=None):
        cmd = self.entry.get().strip()
        if not cmd: return
        self.add_user_message(cmd)
        if cmd.lower() in ["exit", "quit"]:
            self.add_eula_message("Tạm biệt!")
            self.entry.config(state='disabled')
            return
        for line in self.processor.process_command_text(cmd).splitlines():
            line = line.strip()
            if line.startswith(""): line = line[5:].strip()
            if line.startswith(""): line = line[1:].strip()
            if line: self.add_eula_message(line)
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    AssistantGUI(root)
    root.mainloop()