import random

def oan_tu_ti():
    choices = ["kéo", "búa", "bao"]
    print("\n--- Oẳn tù tì ---")
    print("Chọn: kéo, búa, bao")
    user = input("Bạn chọn: ").strip().lower()
    if user not in choices:
        print("Lựa chọn không hợp lệ. Vui lòng chọn: kéo, búa, bao.")
        return
    bot = random.choice(choices)
    print(f"Máy chọn: {bot}")
    if user == bot:
        print("Hòa!")
    elif (user == "kéo" and bot == "bao") or (user == "búa" and bot == "kéo") or (user == "bao" and bot == "búa"):
        print("Bạn thắng!")
    else:
        print("Bạn thua!")

def xo_so_may_man():
    print("\n--- Xổ số may mắn ---")
    try:
        user_number = int(input("Chọn một số may mắn từ 0 đến 99: "))
        if not 0 <= user_number <= 99:
            print("Vui lòng chọn số trong khoảng 0-99.")
            return
    except ValueError:
        print("Vui lòng nhập một số hợp lệ.")
        return
    lucky_number = random.randint(0, 99)
    print(f"Số may mắn là: {lucky_number}")
    if user_number == lucky_number:
        print("Chúc mừng! Bạn đã trúng thưởng!")
    else:
        print("Chúc bạn may mắn lần sau!")

def menu_giaitri():
    while True:
        print("\n=== Menu ===")
        print("1. Oẳn tù tì")
        print("2. Xổ số may mắn")
        print("0. Thoát")
        choice = input("Chọn trò chơi : ").strip()
        if choice == "1":
            oan_tu_ti()
        elif choice == "2":
            xo_so_may_man()
        elif choice == "0":
            print("Tạm biệt! Hẹn gặp lại.\n")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.\n")

if __name__ == "__main__":
    menu_giaitri()