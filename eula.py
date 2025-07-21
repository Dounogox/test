import tkinter as tk
from main import CommandProcessor

class AssistantGUI:
    def __init__(self, root):
        self.processor = CommandProcessor()
        root.title("Eula Chat")
        root.geometry("600x400")
        root.configure(bg="white")

        # Khung chat với tag cho user và Eula
        self.text_area = tk.Text(root, wrap=tk.WORD, state='normal', font=("Consolas", 12), bg="white", fg="black")
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.text_area.tag_configure("eula", foreground="#222", background="#e0ffe0", justify="left", lmargin1=10, lmargin2=10, rmargin=100, spacing3=5)
        self.text_area.tag_configure("user", foreground="#222", background="#cce6ff", justify="right", lmargin1=100, lmargin2=100, rmargin=10, spacing3=5)
        self.text_area.config(state='disabled')

        # Frame nhập lệnh
        input_frame = tk.Frame(root, bg="white")
        input_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        self.entry = tk.Entry(input_frame, font=("Consolas", 12), bg="white", fg="black")
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.entry.bind("<Return>", self.process_input)

        self.send_button = tk.Button(input_frame, text="Gửi", font=("Consolas", 12), command=self.process_input, bg="white")
        self.send_button.pack(side=tk.RIGHT)

        # Chào mừng
        self.add_eula_message("Chào mừng bạn!")

    def add_user_message(self, message):
        self.text_area.config(state='normal')
        self.text_area.insert(tk.END, f"{message}\n", "user")
        self.text_area.config(state='disabled')
        self.text_area.see(tk.END)

    def add_eula_message(self, message):
        self.text_area.config(state='normal')
        self.text_area.insert(tk.END, f"{message}\n", "eula")
        self.text_area.config(state='disabled')
        self.text_area.see(tk.END)

    def process_input(self, event=None):
        command = self.entry.get().strip()
        if not command:
            return
        self.add_user_message(command)
        if command.lower() in ["exit", "quit"]:
            self.add_eula_message("Tạm biệt!")
            self.entry.config(state='disabled')
            self.send_button.config(state='disabled')
            return
        # Lấy kết quả từ CommandProcessor
        result = self.processor.process_command_text(command)
        # Hiển thị từng dòng trả lời của Eula (bỏ tiền tố "Eula:" nếu có)
        for line in result.splitlines():
            line = line.strip()
            if line.startswith("Eula:"):
                line = line[5:].strip()
            if line:
                self.add_eula_message(line)
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AssistantGUI(root)
    root.mainloop()