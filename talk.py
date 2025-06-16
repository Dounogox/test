import random

def simple_chat():
    greetings = [
        "Xin chào!", "Chào bạn!", "Rất vui được gặp bạn!", "Chào mừng bạn quay lại!",
        "Bạn khỏe không?", "Hôm nay bạn thế nào?"
    ]
    farewells = ["Đã tạm dừng trò chuyện. Tôi sẽ tiếp tục thực hiện lệnh"]
    default_responses = [
        "Tôi chưa hiểu ý bạn lắm, bạn có thể nói rõ hơn không?",
        "Bạn muốn hỏi gì nữa không?",
        "Thú vị đấy! Bạn muốn nói thêm gì không?",
        "Tôi luôn sẵn sàng lắng nghe bạn.",
        "Bạn có sở thích gì không?",
        "Bạn thích nghe nhạc hay xem phim?",
        "Bạn có muốn tôi kể chuyện cười không?",
        "Bạn có muốn tôi bully bạn không?",
    ]
    jokes = [
        "Tại sao máy tính không bao giờ đói? Vì nó luôn có ổ cứng!",
        "Con gà nào biết code? Đó là con gà Java!",
        "Vì sao lập trình viên hay buồn? Vì họ thường gặp lỗi!",
        "Tại sao cá không thích internet? Vì sợ bị 'phishing'!",
        "Đi tiểu ở biển là gì? - Sea đái :)))",
        "Tại sao lập trình viên không thích tự nhiên? Vì họ sợ bị 'bug'!",
        "Con ong diễn kịch được gọi là gì? - Bee kịch :)))",
        "Người ta uống sữa bò để làm gì? - Để cow :))))",
        "Đứng trước Bmen là gì? - Amen :)))",
        "Kẻ giết người u sầu đc gọi là gì? - Sad nhân :))))",
        "Đột nhiên béo lên được gọi là gì? - Fat tướng :)))",
        "Ghế nào xa nhất? - Ghế So Far :))",
        "Ngực bên trái được gọi là gì? - Ngực left :)))",
    ]

    print(random.choice(greetings))
    while True:
        user = input("You: ").strip().lower()
        if user in ["tạm biệt", "bye", "end"]:
            print(random.choice(farewells))
            break
        elif any(word in user for word in ["khỏe", "thế nào", "dạo này"]):
            print("Tôi là trợ lý ảo nên lúc nào cũng khỏe! Còn bạn thì sao?")
        elif any(word in user for word in ["tên", "bạn là ai"]):
            print("Tôi là trợ lý ảo của bạn. Bạn có thể gọi tôi là Bố của bạn!")
        elif "cảm ơn" in user:
            print("Không có gì, tôi luôn sẵn sàng giúp bạn!")
        elif "mấy giờ" in user or "thời gian" in user:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M:%S")
            print(f"Bây giờ là {now}")
        elif "kể chuyện cười" in user or "chuyện cười" in user or "vui" in user:
            print("Đây là một chuyện cười cho bạn:")
            print(random.choice(jokes))
        elif "sở thích" in user:
            print("Tôi thích học hỏi những điều mới và giúp đỡ mọi người. Còn bạn?")
        elif "âm nhạc" in user or "nghe nhạc" in user:
            print("Tôi thích nghe nhạc nhẹ nhàng. Bạn thích thể loại nhạc nào?")
        elif "phim" in user:
            print("Tôi thích xem phim khoa học viễn tưởng. Bạn thì sao?")
        else:
            print(random.choice(default_responses))

if __name__ == "__main__":
    simple_chat()