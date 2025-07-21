import tkinter as tk
from main import CommandProcessor

class SimpleAssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Eula Assistant")
        self.root.geometry("400x400")
        self.processor = CommandProcessor()

        # Khung hiển thị hội thoại
        self.chat_box = tk.Text(root, height=20, bg="white", fg="black", state="disabled", wrap=tk.WORD)
        self.chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Khung nhập lệnh
        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack(fill=tk.X, padx=10, pady=5)

        self.input_entry = tk.Text(self.entry_frame, height=1, font=("Segoe UI", 11), wrap="none")
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.input_entry.bind("<Return>", self.handle_enter)

        self.send_button = tk.Button(self.entry_frame, text="Gửi", command=self.handle_enter)
        self.send_button.pack(side=tk.RIGHT)

        self.display("Eula", "Chào mừng bạn!")

    def display(self, sender, message):
        self.chat_box.configure(state="normal")
        # Nếu message đã có "Eula :" ở đầu thì không cần thêm nữa
        if sender == "Eula" and message.strip().startswith("Eula :"):
            self.chat_box.insert(tk.END, f"{message.strip()}\n")
        else:
            self.chat_box.insert(tk.END, f"{sender}: {message.strip()}\n")
        self.chat_box.configure(state="disabled")
        self.chat_box.see(tk.END)


    def handle_enter(self, event=None):
        user_input = self.input_entry.get("1.0", tk.END).strip()
        if not user_input:
            return
        self.display("You", user_input)
        self.input_entry.delete("1.0", tk.END)

        try:
            response = self.processor.process_command_text(user_input)
            if response.strip():
                self.display("Eula", response.strip())
        except Exception as e:
            self.display("Eula", f"Lỗi: {str(e)}")
        return "break"  # Ngăn Text xuống dòng khi nhấn Enter


if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleAssistantGUI(root)
    root.mainloop()
