# Manba Xazratov Behro'z
class TournamentScoringSystem:
    def __init__(self):
        self.teams = {}
        self.scores = {}
        self.players = {}
        self.messages = []
    

    def start(self):
        print("♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦")
        print("♦  ⚠️  Turnir boshlandi                                  ♦")
        print("♦  1️⃣  Yakka tartibda qatnashish                         ♦")
        print("♦  2️⃣  Jamoa bo'lib qatnashish                           ♦")
        print("♦  3️⃣  Umumiy jamoalar ballarini ko'rish                 ♦")
        print("♦  4️⃣  Yakka tartibdagilar ballarini ko'rish             ♦")
        print("♦  5️⃣  Shartlar va berilgan ballar bilan tanishish       ♦")
        print("♦  6️⃣  Ishtirokchining balini o'zgartirish               ♦")
        print("♦  7️⃣  Xat yo'llash                                      ♦")
        print("♦  8️⃣  Chiqish                                           ♦")
        print("♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦")

# ishtirokchi qo'shish 
    def player(self):
        try:
            for num in range(1,20+1):
                players_name = input(f"{num} chi ishtirokchi ismingizni kiriting: ")
                how_much = int(input("Shartlar nechta bo'lishini xoxlaysiz? "))
                if players_name in self.players:
                    print("✔ ishtirokchi allaqachon ishtirok etyabdi")
                    break
                else:
                    self.players[players_name] = 0
                    for num2 in range(1,how_much+1):
                        shart = input(f"{num2} chi shartni kiriting: ")
                        ball = int(input(f"{num2} shartga nechi ball qo'yasiz: "))
                        self.scores[shart] = ball
                        print(f"{shart} ga {ball} ball qo'yiladi")
                        print(f"{players_name} shartni bajarishga ketdi")
                        option = int(input(f"{players_name} shartni bajardimi?\n1. xa\n2. yo'q\n(1/2): "))  
                        if option == 1:
                            self.players[players_name]+=ball
                        else:
                            print(f"{players_name} shartni bajarmadi va ball olmadi 🤷‍♀️")
        except ValueError:
            print("faqat raqam kiritish mumkin")
        print(f"ishtirokchi ballari: {self.players} ")

# jamoa qo'shish               

    def team(self):
        try:
            for num_2 in range(1,4+1):
                teams_name = input(f"{num_2} chi Jamoa nomini kiriting: ")
                how_much = int(input("Shartlar nechta bo'lishini xoxlaysiz? "))
                if teams_name in self.teams:
                    print("✔ Jamoa allaqachon ishtirok etyabdi")
                    break
                else:
                    self.teams[teams_name] = 0
                    for num3 in range(1,how_much+1):
                        shart = input(f"{num3} chi shartni kiriting: ")
                        ball = int(input(f"{num3} shartga nechi ball qo'yasiz: "))
                        self.scores[shart] = ball
                        print(f"{shart} ga {ball} ball qo'yiladi")
                        print(f"{teams_name} shartni bajarishga ketdi")
                        option = int(input(f"{teams_name} shartni bajardimi?\n1. xa\n2. yo'q: "))  
                        if option == 1:
                            self.teams[teams_name]+=ball
                        else:
                            print(f"{teams_name} shartni bajarmadi va ball olmadi")
        except ValueError:
            print("faqat raqam kiritilsin")
        print(f"Jamoa ballari: {self.teams} ")
        



# ishtirokchining balini o'zgartirish
    def updateBall(self):
        update__player = input("Balini o'zgartirmoqchi bo'lgan ishtirokchi ismini kiriting: ")
        if update__player in self.players:
            current__ball = int(input("ishtirokchining yangi balini kiriting: "))
            self.players[update__player] = current__ball
            print(f"{update__player} ishtirokchini bali {current__ball} ga o'zgartirildi!")
        
        else:
            print("bunday ishtirokchi mavjud emas!")

# jamoa umumiy ballari 
    def overallOfteam(self):
        print(f"jamoa umumiy ballari: {self.teams}")
        
# ishtirokchi umumiy ballari    
    def overallOfplayer(self):
        print(f"ishtirokchilar umumiy ballari: {self.players}")

# Shartlar va berilgan ballar
    def overall(self):
        print(f"Shartlar va berilgan ballar: {self.scores}")

# xat yo'llash
    def message(self):
        from_user = input("ishtirokchi ismingizni kiriting: ")
        message_user = input("Dastur haqida fikr mulohazalaringizni yozishingiz mumkin: ") 
        overall__message = message_user+f" {from_user} dan kelgan xabar!"
        self.messages.append(overall__message)
        print(f"foydalanuvchi habari: {self.messages}")

def main():
    system = TournamentScoringSystem()
    while True:
        system.start()
        choice = input("Variantni tanlang: ")

        if choice == "1":
            system.player()
        elif choice == "2":
            system.team()
        elif choice == "3":
            system.overallOfteam()
        elif choice == "4":
            system.overallOfplayer()
        elif choice == "5":
            system.overall()
        elif choice == "6":
            system.updateBall()
        elif choice == "7":
            system.message()
        elif choice == "8":
            print("tizimdan chiqildi. xayr!")
            break
        else:
            print("Notog'ri variant. qayta urinib ko'ring")


if __name__ == "__main__":
    main()
