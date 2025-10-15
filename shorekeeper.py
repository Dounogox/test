# filepath: c:\codesieungu\shorekeeper\shorekeeper.py
from PyQt5 import QtWidgets, QtGui, QtCore
from main import CommandProcessor
import html

class AssistantGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.processor = CommandProcessor()
        self.setWindowTitle("Shorekeeper")
        self.setWindowIcon(QtGui.QIcon("shore.ico"))
        self.setGeometry(100, 100, 1030, 640)

        self.setStyleSheet("background: white;")
        # load background image (đổi đường dẫn tới ảnh của bạn)
        self.bg_pixmap = QtGui.QPixmap(r"c:\codesieungu\shorekeeper\wall2.png")

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        # tạo QTextEdit trước khi cấu hình style cho nó
        self.text_area = QtWidgets.QTextEdit(self)
        self.text_area.setReadOnly(True)
        self.text_area.setFont(QtGui.QFont("Consolas", 12))
        # làm cho vùng chat bán trong suốt để thấy ảnh nền
        self.text_area.setStyleSheet("background: rgba(255,255,255,0); color: black; border: none;")
        layout.addWidget(self.text_area, stretch=1)

        input_frame = QtWidgets.QFrame(self)
        input_frame.setStyleSheet("""
            QFrame {
                background: white;
                border-radius: 12px;
                border: 1px solid #e0e0e0;
            }
        """)
        input_layout = QtWidgets.QHBoxLayout(input_frame)
        input_layout.setContentsMargins(8, 8, 8, 8)
        input_layout.setSpacing(8)

        self.entry = QtWidgets.QLineEdit(input_frame)
        self.entry.setFont(QtGui.QFont("Consolas", 12))
        self.entry.setStyleSheet("background: white; color: black; border: none;")
        self.entry.returnPressed.connect(self.process_input)
        input_layout.addWidget(self.entry, stretch=1)

        self.send_btn = QtWidgets.QPushButton("Gửi", input_frame)
        self.send_btn.setFont(QtGui.QFont("Consolas", 12))
        self.send_btn.setStyleSheet("""
            QPushButton {
                background: blue;
                color: white;
                border-radius: 12px;
                border: 1px solid #e0e0e0;
                padding: 6px 18px;
            }
            QPushButton:hover {
                background: #f0f0f0;
            }
        """)
        self.send_btn.clicked.connect(self.process_input)
        input_layout.addWidget(self.send_btn)

        layout.addWidget(input_frame, stretch=0)

        self.add_shorekeeper_message("Chào mừng bạn!")

    def add_user_message(self, message):
        safe = html.escape(message).replace("\n", "<br>")
        self.text_area.append(
            f'<table width="100%" cellpadding="2" style="border-collapse:collapse; margin:6px 2px;">'
            f'  <tr>'
            f'    <td width="60%"></td>'
            f'    <td align="right" style="vertical-align:top; padding-left:8px;">'
            f'      <div style="display:inline-block; background:#e6f0ff; color:#003366; '
            f'border:3px solid #2b6fda; padding:10px 14px; max-width:60%; '
            f'word-wrap:break-word; text-align:right; font-weight:600;">'
            f'{safe}</div>'
            f'    </td>'
            f'  </tr>'
            f'</table>'
        )

    def add_shorekeeper_message(self, message):
        safe = html.escape(message).replace("\n", "<br>")
        self.text_area.append(
            f'<table width="50%" cellpadding="2" style="border-collapse:collapse; margin:6px 2px;">'
            f'  <tr>'
            f'    <td align="left" style="vertical-align:top; padding-right:8px;">'
            f'      <div style="display:inline-block; background:#f8f8f8; color:#000; '
            f'border:3px solid #8f8f8f; padding:10px 14px; max-width:80%; '
            f'word-wrap:break-word; text-align:left; font-weight:600;">'
            f'{safe}</div>'
            f'    </td>'
            f'    <td width="40%"></td>'
            f'  </tr>'
            f'</table>'
        )

    def process_input(self):
        cmd = self.entry.text().strip()
        if not cmd:
            return
        self.add_user_message(cmd)
        if cmd.lower() in ["exit", "quit"]:
            self.add_shorekeeper_message("Tạm biệt!")
            self.entry.setDisabled(True)
            self.send_btn.setDisabled(True)
            return
        for line in self.processor.process_command_text(cmd).splitlines():
            line = line.strip()
            if line.startswith("Shorekeeper"):
                line = line.split(":", 1)[-1].strip()
            if line.startswith(":"):
                line = line[1:].strip()
            if line:
                self.add_shorekeeper_message(line)
        self.entry.clear()

    def paintEvent(self, event):
        # vẽ ảnh nền scale theo kích thước cửa sổ (giữ tỉ lệ, cắt tràn nếu cần)
        painter = QtGui.QPainter(self)
        if getattr(self, "bg_pixmap", None) and not self.bg_pixmap.isNull():
            pix = self.bg_pixmap.scaled(self.size(), QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation)
            # center the pixmap
            x = (self.width() - pix.width()) // 2
            y = (self.height() - pix.height()) // 2
            painter.drawPixmap(x, y, pix)
        super().paintEvent(event)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = AssistantGUI()
    window.show()
    sys.exit(app.exec_())