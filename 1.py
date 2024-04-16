from random import randint, choice

# список назв мечів
SWORD_NAMES = [
        "Меч Смертівника",
        "Драконобійчий Клинок",
        "Стрілецька Сага",
        "Кований Піднебінник",
        "Тіньовий Катана",
        "Ластівчиний Клинок",
        "Зоряний Рапір",
        "Проклятий Кинджал",
        "Молот Богів",
        "Легендарний Лезо",
        "Гнів Берсерка",
        "Вогняний Розрив",
        "Лісовий Сокирян",
        "Чорний Рубіж",
        "Лютівний Гак",
        "Кам'яний Розтрощувач",
        "Драконячий Топір",
        "Палаючий Клин",
        "Буревій Сокира",
        "Королівський Відламник"]

# Опис класу Swords
class Swords:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity
        self.player = None
        self.player_buff = None
        self.vitality = randint(10, 20)

    @staticmethod
    def create_random_rarity(name):
        rarity = choice(["Common", "Rare", "Epic"])
        return Swords(name, rarity)

    def apply_bonus(self):
        return f"{self.name} з рідкістю {self.rarity}"

    def get_buff_damag(self, amount):
        self.vitality += amount

    def get_buff_vitality(self, amount):
        self.vitality += amount

    def aging(self):
        return "Меч зношується."

    def expired_buff(self):
        return "Баф втрачено."

    def repair(self):
        return "Меч підлеглість ремонту."

    def attack(self, opponent):
        opponent.vitality -= randint(1, 10)
        if opponent.vitality < 0:
            opponent.vitality = 0
        print(f"{self.name} атакує {opponent.name}!")

def create_players() -> Swords:
    """Функція для створення гравців та їх мечів"""
    while True:
        player_name = input("Введіть ім'я гравця: ")
        if len(player_name) >= 2:  # Перевірка, чи ім'я гравця має хоча б дві букви
            break
        else:
            print("Ім'я гравця повинно містити принаймні дві букви. Спробуйте ще раз.")

    # Створення меча для гравця та випадкова назва
    s = Swords.create_random_rarity(choice(SWORD_NAMES))
    print(s.apply_bonus())
    s.player = player_name
    print(f"Гравець {player_name} отримує Меч:", s.apply_bonus())
    return s

def select_buff(player_name: str) -> str:
    """Функція для вибору бафу гравцем."""
    buff = input(f"{player_name}, введіть 1 для бафу на атаку, 2 для бафу на міцність, будь-яка кнопка щоб пропустити: ")
    if buff in ["1", "2"]:
        return buff
    print("Помилка: Потрібно ввести 1 або 2. Гравець пропускає хід.")
    return None

# Виконання програми
if __name__ == "__main__":
    print("Початок гри:")
    c = create_players()
    d = create_players()

    c.player_buff = select_buff(c.player)
    d.player_buff = select_buff(d.player)

    for pb in [c, d]:
        if pb.player_buff == "1":
            print(f"{pb.player} застосовує баф на атаку:")
            pb.get_buff_damag(randint(2, 5))
        elif pb.player_buff == "2":
            print(f"{pb.player} застосовує баф на міцність:")
            pb.get_buff_vitality(randint(6, 12))
        else:
            print("Введено неправильне значення, тому баф не застосовується!")
        print(pb.aging(), pb.apply_bonus())

    while c.vitality > 0 and d.vitality > 0:
        print("Новий раунд:")
        c.attack(d)
        print(f"{c.player} з {c.name} атакує {d.player} з {d.name}")
        d.attack(c)
        print(f"{d.player} з {d.name} відповідає на атаку {c.player} з {c.name}")
        print(f"Закінчилися бафи: {c.expired_buff()} ||||| {d.expired_buff()}")
        print(f"<<<<< {c.name} {c.vitality} ||||| {d.name} {d.vitality} >>>>>>")
        print(f"Починаємо ремонтувати мечі: {c.repair()} ||||| {d.repair()}")
        print(f"<<<<< {c.name} {c.vitality} ||||| {d.name} {d.vitality} >>>>>>")

    if c.vitality > 0 and c.vitality >= d.vitality:
        print(f"Гравець {c.player} переміг над {d.player}")
    else:
        print(f"Гравець {d.player} переміг над {c.player}")

    print("Гра закінчена.")
