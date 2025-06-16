import hello
import talk
import search
import app
import giaitri
from typing import Optional

#thực hiện lệnhlệnh
class CommandProcessor:
    def __init__(self):
        self.search_patterns = search.mau_google + search.mau_youtube
        self.app_patterns = app.tu_khoa_mo_app
        self.greeting_patterns = ["hi", "hello", "chào", "xin chào"]
        self.giaitri_patterns = ["giải trí", "trò chơi", "entertainment"]
        self.talk_patterns = ["nói chuyện", "trò chuyện", "chat", "talk"]

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
        for pattern in self.talk_patterns:
            if pattern in command:
                return "talk"
        return "unknown"

    def show_menu(self):
        """Hiển thị menu chức năng"""
        print("Tôi có thể :")
        print("- Nói chuyện đơn giản")
        print("- Mở ứng dụng (vd: 'mở chrome')")
        print("- Tìm kiếm Google (vd: 'what is python')")
        print("- Tìm video YouTube (vd: 'play video music')")
        print("- Chơi trò giải trí (vd: 'giải trí', 'trò chơi')")
        print("- Dùng lệnh \"help\" để xem hướng dẫn\n")
        print("Nhập 'exit' hoặc 'quit' để thoát\n")

    def get_menu_text(self) -> str:
        return (
            "Tôi có thể :\n"
            "- Nói chuyện đơn giản\n"
            "- Mở ứng dụng (vd: 'mở chrome')\n"
            "- Tìm kiếm Google (vd: 'what is python')\n"
            "- Tìm video YouTube (vd: 'play video music')\n"
            "- Chơi trò giải trí (vd: 'giải trí', 'trò chơi')\n"
            "- Dùng lệnh \"help\" để xem hướng dẫn\n"
            "Nhập 'exit' hoặc 'quit' để thoát\n"
        )

    def print_help(self):
            """In nội dung file help.txt ra màn hình"""
            try:
                with open("help.txt", "r", encoding="utf-8") as f:
                    print(f.read())
            except Exception as e:
                print("Không thể đọc file hướng dẫn:", e)

    def execute_command(self, command: str) -> Optional[str]:
        """Thực thi lệnh theo loại phù hợp"""
        command_type = self.detect_command_type(command)
        if command_type == "greeting":
            hello.chaohoi()
            self.show_menu()
            return None
        elif command_type == "help":
            self.print_help()
            return None
        elif command_type == "app":
            app.xu_ly_lenh_mo_app(command)
            return None
        elif command_type == "search":
            search.tro_ly_tim_kiem(command)
            return None
        elif command_type == "giaitri":
            giaitri.menu_giaitri()
            return None
        elif command_type == "talk":
            talk.simple_chat()
            return None
        return "\nKhông hiểu lệnh này. Vui lòng thử lại.\n"

    def process_command_text(self, command: str) -> str:
        import io
        import sys
        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()
        self.execute_command(command)
        sys.stdout = old_stdout
        return mystdout.getvalue()

#### ko quan trọng
def main():
    processor = CommandProcessor()
    print("Chào mừng bạn!")
    processor.show_menu()
    while True:
        try:
            command = input("You : ").strip()
            if command.lower() in ["exit", "quit"]:
                print("\nTạm biệt!")
                break
            result = processor.execute_command(command)
            if result:
                print(result)
        except Exception as e:
            print(f"Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    main()