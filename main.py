import hello
import search
import app
import giaitri
import ai
from typing import Optional

#thực hiện lệnhlệnh
class CommandProcessor:
    def __init__(self):
        self.search_patterns = search.mau_google + search.mau_youtube
        self.app_patterns = app.tu_khoa_mo_app
        self.greeting_patterns = ["hi", "hello", "chào", "xin chào"]
        self.giaitri_patterns = ["giải trí", "trò chơi", "entertainment"]
        self.ai_patterns = ["ai", "hỏi ai", "chat ai"]

    def detect_command_type(self, command: str) -> str:
        """Phát hiện loại lệnh dựa trên từ khóa"""
        command = command.lower().strip()
        # Kiểm tra lệnh chào hỏi
        if command in self.greeting_patterns:
            return "greeting"
        # Xem hướng dẫn sử dụng
        if command == "help":
            return "help"
        # Kiểm tra lệnh mở ứng dụng
        for pattern in self.app_patterns:
            if pattern in command:
                return "app"
        # Kiểm tra lệnh tìm kiếm
        for pattern in self.search_patterns:
            if pattern in command:
                return "search"
        for pattern in self.giaitri_patterns:
            if pattern in command:
                return "giaitri"
        for pattern in self.ai_patterns:
            if command.startswith(pattern):
                return "ai"
        return "ai"

    def print_help(self):
        """In nội dung file help.txt ra màn hình"""
        try:
            with open("help.txt", "r", encoding="utf-8") as f:
                for line in f:
                    print("Eula :", line.strip())
        except Exception as e:
            print("Eula :", "Không thể đọc file hướng dẫn:", e)

    def execute_command(self, command: str) -> Optional[str]:
        """Thực thi lệnh theo loại phù hợp"""
        command_type = self.detect_command_type(command)
        if command_type == "greeting":
            print("Eula :", end=" ")
            hello.chaohoi()
            return None
        elif command_type == "help":
            print("Eula :", end=" ")
            self.print_help()
            return None
        elif command_type == "app":
            print("Eula :", end=" ")
            app.xu_ly_lenh_mo_app(command)
            return None
        elif command_type == "search":
            print("Eula :", end=" ")
            search.tro_ly_tim_kiem(command)
            return None
        elif command_type == "giaitri":
            print("Eula :", end=" ")
            giaitri.menu_giaitri()
            return None
        elif command_type == "ai":
            self.ai_chat(command)
            return None
        print("Eula : Không hiểu lệnh này. Vui lòng thử lại.\n")

    def process_command_text(self, command: str) -> str:
        import io
        import sys
        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()
        self.execute_command(command)
        sys.stdout = old_stdout
        return mystdout.getvalue()

    def ai_chat(self, command: str):
        # Nếu bắt đầu bằng từ khóa AI thì bỏ từ khóa đi, còn lại giữ nguyên
        for pattern in self.ai_patterns:
            if command.startswith(pattern):
                prompt = command[len(pattern):].strip()
                break
        else:
            prompt = command
        if not prompt:
            print("Eula : Bạn cần nhập nội dung câu hỏi.")
            return
        response_text = ai.ask_ai(prompt)
        print("Eula :", response_text)
#### ko quan trọng
def main():
    processor = CommandProcessor()
    print("Chào mừng bạn!\n")
    while True:
        try:
            command = input("You : ").strip()
            if command.lower() in ["exit", "quit"]:
                print("\nTạm biệt!\n")
                break
            result = processor.execute_command(command)
            if result:
                print(result)
        except Exception as e:
            print(f"Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    main()