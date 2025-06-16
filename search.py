import webbrowser
import urllib.parse

# Mẫu câu hỏi Google
mau_google = [
    "what is", "how to", "where is", "why does", "how does", "when is", "who is",
    "what are", "how can", "how do", "why is", "how much", "how many", "can you",
    "should i", "is it", "does it", "do you", "what does", "where can",
    "làm thế nào để", "tại sao", "cái gì là", "ai là", "ở đâu", "bao nhiêu", "khi nào",
    "tôi nên", "có phải", "cách để", "vì sao", "sao lại", "để làm gì","search"
]

# Mẫu lệnh YouTube
mau_youtube = [
    "play song", "find video", "search youtube for", "play video", "watch",
    "mở video", "phát nhạc", "tìm video", "xem", "nghe bài", "tìm youtube"
]

def tro_ly_tim_kiem(cau_lenh: str):
    cau_lenh_lower = cau_lenh.lower().strip()

    # Kiểm tra lệnh YouTube trước
    for mau in mau_youtube:
        if mau in cau_lenh_lower:
            start_index = cau_lenh_lower.find(mau)
            noi_dung = cau_lenh_lower[start_index + len(mau):].strip()
            if noi_dung:
                url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus(noi_dung)
                webbrowser.open(url)
                print(f"\nĐang mở : {noi_dung}\n")
            else:
                print("\nKhông có nội dung để tìm trên YouTube.\n")
            return

    # Kiểm tra lệnh Google
    for mau in mau_google:
        if mau in cau_lenh_lower:
            start_index = cau_lenh_lower.find(mau)
            cau_truy_van = cau_lenh_lower[start_index:].strip()
            url = "https://www.google.com/search?q=" + urllib.parse.quote_plus(cau_truy_van)
            webbrowser.open(url)
            print(f"\nĐang tìm : {cau_truy_van}\n")
            return

    print("\nKhông xác định được nền tảng tìm kiếm phù hợp.\n")
