import os
import subprocess
import shutil
from difflib import get_close_matches
import winreg

# Từ khóa mở app
tu_khoa_mo_app = ["open app", "mở app", "open", "mở"]

# Các thư mục thường chứa ứng dụng
search_dirs = [
    os.environ.get("ProgramFiles", ""),
    os.environ.get("ProgramFiles(x86)", ""),
    os.environ.get("LOCALAPPDATA", "") + "\\Programs",
    "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs",
    os.path.expanduser("~\\Desktop"),
    "C:\\Users\\Public\\Desktop",
    os.environ.get("APPDATA", "") + "\\Microsoft\\Windows\\Start Menu\\Programs",
    "C:\\Users\\Public\\Start Menu\\Programs",
    "C:\\Windows\\System32",
    "C:\\Windows\\SysWOW64"
]

def get_installed_apps_from_registry():
    """
    Lấy danh sách ứng dụng từ Registry Windows
    """
    apps = []
    reg_paths = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    ]
    
    for reg_path in reg_paths:
        try:
            registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_READ)
            for i in range(0, winreg.QueryInfoKey(registry_key)[0]):
                try:
                    subkey_name = winreg.EnumKey(registry_key, i)
                    subkey = winreg.OpenKey(registry_key, subkey_name)
                    try:
                        install_location = winreg.QueryValueEx(subkey, "InstallLocation")[0]
                        if install_location and os.path.exists(install_location):
                            search_dirs.append(install_location)
                    except:
                        pass
                    winreg.CloseKey(subkey)
                except WindowsError:
                    break
            winreg.CloseKey(registry_key)
        except WindowsError:
            continue


def tim_ung_dung_trong_he_thong(ten_ung_dung: str):
    """
    Tìm ứng dụng .exe hoặc .lnk gần giống với tên yêu cầu.
    """
    ten_ung_dung = ten_ung_dung.lower()
    
    # Thử tìm trong PATH trước
    path = shutil.which(ten_ung_dung)
    if path:
        return path

    # Cập nhật danh sách ứng dụng từ Registry
    get_installed_apps_from_registry()
    
    file_candidates = []
    for base_dir in search_dirs:
        if not os.path.exists(base_dir):
            continue
        try:
            for root, _, files in os.walk(base_dir):
                for file in files:
                    if file.lower().endswith((".exe", ".lnk")):
                        file_name = os.path.splitext(file)[0].lower()
                        full_path = os.path.join(root, file)
                        file_candidates.append((file_name, full_path))
        except PermissionError:
            continue

    # Tìm kiếm với độ chính xác cao hơn
    matches = get_close_matches(ten_ung_dung, [f[0] for f in file_candidates], n=5, cutoff=0.5)
    
    if matches:
        # Trả về kết quả khớp nhất
        for name, path in file_candidates:
            if name == matches[0]:
                return path
                
    # Tìm kiếm mờ nếu không tìm thấy kết quả chính xác
    for name, path in file_candidates:
        if ten_ung_dung in name:
            return path
            
    return None

def mo_ung_dung_thong_minh(ten_ung_dung: str):
    """
    Mở ứng dụng Windows bằng tên gần đúng, không cần app_map.
    """
    duong_dan = tim_ung_dung_trong_he_thong(ten_ung_dung)
    if duong_dan:
        subprocess.Popen(duong_dan, shell=True)
        print(f"Đã mở ứng dụng {ten_ung_dung}\n")
    else:
        print(f"Không tìm thấy ứng dụng '{ten_ung_dung}'.\n")

def xu_ly_lenh_mo_app(cau_lenh: str):
    """
    Xử lý câu lệnh kiểu: 'mở app ...', 'open ...', v.v.
    """
    cau_lenh_lower = cau_lenh.lower().strip()
    for tu_khoa in tu_khoa_mo_app:
        if tu_khoa in cau_lenh_lower:
            ten_app = cau_lenh_lower.replace(tu_khoa, "", 1).strip()
            if ten_app:
                mo_ung_dung_thong_minh(ten_app)
            else:
                print("Bạn chưa nhập tên ứng dụng.\n")
            return
    print("Câu lệnh không chứa từ khóa mở ứng dụng.\n")