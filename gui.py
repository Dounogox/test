import tkinter as tk
from main import CommandProcessor

class AssistantGUI:
    def __init__(self, root):
        self.processor = CommandProcessor()
        root.title("Trợ lý ảo")
        root.geometry("500x600")
        root.configure(bg="#222222")

        # Khung hiển thị chat
        self.text_area = tk.Text(
            root, wrap=tk.WORD, state='normal', font=("Consolas", 13),
            bg="#222222", fg="#f1f1f1", insertbackground="#f1f1f1", bd=0, relief=tk.FLAT
        )
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.text_area.insert(tk.END, "Chào mừng bạn\n" + self.processor.get_menu_text())
        self.text_area.config(state='disabled')

        # Frame chứa ô nhập và nút gửi ở dưới cùng
        input_frame = tk.Frame(root, bg="#222222")
        input_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        # Ô nhập lệnh
        self.entry = tk.Entry(input_frame, font=("Consolas", 13), bg="#333333", fg="#f1f1f1", insertbackground="#f1f1f1")
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.entry.bind("<Return>", self.process_input)

        # Nút gửi
        self.send_button = tk.Button(
            input_frame, text="->", font=("Consolas", 13, "bold"),
            bg="#444444", fg="#f1f1f1", activebackground="#666666",
            command=self.process_input, width=4, borderwidth=0
        )
        self.send_button.pack(side=tk.RIGHT)

    def process_input(self, event=None):
        command = self.entry.get().strip()
        if not command:
            return
        self.text_area.config(state='normal')
        self.text_area.insert(tk.END, f"\nBạn: {command}\n")
        if command.lower() in ["exit", "quit"]:
            self.text_area.insert(tk.END, "\nTạm biệt!\n")
            self.text_area.config(state='disabled')
            self.entry.config(state='disabled')
            self.send_button.config(state='disabled')
            return
        # Lấy kết quả từ CommandProcessor, luôn là chuỗi
        result = self.processor.process_command_text(command)
        if result:
            self.text_area.insert(tk.END, result + "\n")
        self.text_area.see(tk.END)
        self.text_area.config(state='disabled')
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AssistantGUI(root)
    root.mainloop()