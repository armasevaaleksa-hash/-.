# Лабораторна робота №2. Створення та використання функцій, реалізація рекурсії
# Варіант: 1
# ПІБ: Армашева Олександра Іванівна

# Тут має бути Ваш код
print("Hello, World!")

from functools import reduce
# ==========================================================
# RPG CHARACTER ANALYZER
# ==========================================================

characters = [
    {
        "Name": "Death Knight",
        "Level": 55,
        "Health": 6100,
        "Phy_melee_DPS": 980,
        "Phy_range_DPS": 0,
        "Magic_melee_DPS": 678,
        "Magic_range_DPS": 670,
        "Magic_resist": 970,
        "Physical_resist": 875
    },
    {
        "Name": "Paladin",
        "Level": 62,
        "Health": 4900,
        "Phy_melee_DPS": 1420,
        "Phy_range_DPS": 0,
        "Magic_melee_DPS": 620,
        "Magic_range_DPS": 590,
        "Magic_resist": 840,
        "Physical_resist": 720
    },
    {
        "Name": "Warrior",
        "Level": 14,
        "Health": 1180,
        "Phy_melee_DPS": 260,
        "Phy_range_DPS": 100,
        "Magic_melee_DPS": 0,
        "Magic_range_DPS": 0,
        "Magic_resist": 150,
        "Physical_resist": 130
    },
    {
        "Name": "Priest",
        "Level": 26,
        "Health": 1400,
        "Phy_melee_DPS": 140,
        "Phy_range_DPS": 0,
        "Magic_melee_DPS": 550,
        "Magic_range_DPS": 700,
        "Magic_resist": 260,
        "Physical_resist": 240
    },
    {
        "Name": "Shaman",
        "Level": 48,
        "Health": 3690,
        "Phy_melee_DPS": 350,
        "Phy_range_DPS": 160,
        "Magic_melee_DPS": 1080,
        "Magic_range_DPS": 920,
        "Magic_resist": 580,
        "Physical_resist": 660
    },
    {
        "Name": "Warlock",
        "Level": 45,
        "Health": 3000,
        "Phy_melee_DPS": 300,
        "Phy_range_DPS": 0,
        "Magic_melee_DPS": 880,
        "Magic_range_DPS": 920,
        "Magic_resist": 440,
        "Physical_resist": 330
    },
    {
        "Name": "Mage",
        "Level": 34,
        "Health": 2100,
        "Phy_melee_DPS": 140,
        "Phy_range_DPS": 0,
        "Magic_melee_DPS": 520,
        "Magic_range_DPS": 760,
        "Magic_resist": 280,
        "Physical_resist": 310
    },
    {
        "Name": "Rogue",
        "Level": 73,
        "Health": 4700,
        "Phy_melee_DPS": 720,
        "Phy_range_DPS": 650,
        "Magic_melee_DPS": 360,
        "Magic_range_DPS": 320,
        "Magic_resist": 620,
        "Physical_resist": 580
    },
    {
        "Name": "Hunter",
        "Level": 47,
        "Health": 4600,
        "Phy_melee_DPS": 400,
        "Phy_range_DPS": 780,
        "Magic_melee_DPS": 300,
        "Magic_range_DPS": 460,
        "Magic_resist": 480,
        "Physical_resist": 470
    },
    {
        "Name": "Druid",
        "Level": 55,
        "Health": 4500,
        "Phy_melee_DPS": 870,
        "Phy_range_DPS": 200,
        "Magic_melee_DPS": 600,
        "Magic_range_DPS": 830,
        "Magic_resist": 700,
        "Physical_resist": 670
    },
     {
        "Name": "Demon Hunter",
        "Level": 58,
        "Health": 5800,
        "Phy_melee_DPS": 1100,
        "Phy_range_DPS": 250,
        "Magic_melee_DPS": 650,
        "Magic_range_DPS": 400,
        "Magic_resist": 750,
        "Physical_resist": 320
    },
    {
        "Name": "Monk",
        "Level": 53,
        "Health": 5000,
        "Phy_melee_DPS": 1250,
        "Phy_range_DPS": 100,
        "Magic_melee_DPS": 450,
        "Magic_range_DPS": 300,
        "Magic_resist": 800,
        "Physical_resist": 410
    },
    {
        "Name": "Evoker",
        "Level": 60,
        "Health": 4900,
        "Phy_melee_DPS": 200,
        "Phy_range_DPS": 150,
        "Magic_melee_DPS": 750,
        "Magic_range_DPS": 1250,
        "Magic_resist": 1050,
        "Physical_resist": 900
    },
    {
        "Name": "Necromancer",
        "Level": 57,
        "Health": 4000,
        "Phy_melee_DPS": 150,
        "Phy_range_DPS": 100,
        "Magic_melee_DPS": 850,
        "Magic_range_DPS": 1650,
        "Magic_resist": 500,
        "Physical_resist": 600
    },
    {
        "Name": "Berserker",
        "Level": 56,
        "Health": 7200,
        "Phy_melee_DPS": 1350,
        "Phy_range_DPS": 200,
        "Magic_melee_DPS": 100,
        "Magic_range_DPS": 0,
        "Magic_resist": 1300,
        "Physical_resist": 940
    },
    {
        "Name": "Assassin",
        "Level": 27,
        "Health": 1100,
        "Phy_melee_DPS": 500,
        "Phy_range_DPS": 170,
        "Magic_melee_DPS": 150,
        "Magic_range_DPS": 50,
        "Magic_resist": 200,
        "Physical_resist": 100
    },
    {
        "Name": "Templar",
        "Level": 15,
        "Health": 900,
        "Phy_melee_DPS": 160,
        "Phy_range_DPS": 0,
        "Magic_melee_DPS": 200,
        "Magic_range_DPS": 160,
        "Magic_resist": 102,
        "Physical_resist": 52
    },
    {
        "Name": "Elementalist",
        "Level": 70,
        "Health": 4600,
        "Phy_melee_DPS": 100,
        "Phy_range_DPS": 150,
        "Magic_melee_DPS": 950,
        "Magic_range_DPS": 1450,
        "Magic_resist": 1150,
        "Physical_resist": 900
    },
    {
        "Name": "Bard",
        "Level": 32,
        "Health": 1400,
        "Phy_melee_DPS": 350,
        "Phy_range_DPS": 700,
        "Magic_melee_DPS": 450,
        "Magic_range_DPS": 850,
        "Magic_resist": 300,
        "Physical_resist": 560
    },
    {
        "Name": "Dark Ranger",
        "Level": 9,
        "Health": 860,
        "Phy_melee_DPS": 120,
        "Phy_range_DPS": 500,
        "Magic_melee_DPS": 170,
        "Magic_range_DPS": 234,
        "Magic_resist": 85,
        "Physical_resist": 68
    }
]


# ==========================================================
# 1. ЗВИЧАЙНА ФУНКЦіЯ
# ==========================================================

def calculate_damage(character):

    physical = (
        character["Phy_melee_DPS"]
        + character["Phy_range_DPS"]
    )

    magic = (
        character["Magic_melee_DPS"]
        + character["Magic_range_DPS"]
    )

    return physical + magic


# ==========================================================
# 2. ЗВИЧАЙНА ФУНКЦіЯ
# ==========================================================

def calculate_power(character):

    power = (
        character["Level"]
        + character["Health"] / 100
        + calculate_damage(character)
        + character["Magic_resist"] / 100
        + character["Physical_resist"] / 100
    )

    return round(power, 2)


# ==========================================================
# 3. ФУНКЦіЯ С ПАРАМЕТРАМИ ЗА ЗАМОВЧУВАННЯМ
# ==========================================================

def create_character(
        name,
        level=1,
        health=1000,
        phy_melee=100,
        phy_range=0,
        magic_melee=50,
        magic_range=0,
        magic_resist=1000,
        physical_resist=1000
):
    return {
        "Name": name,
        "Level": level,
        "Health": health,
        "Phy_melee_DPS": phy_melee,
        "Phy_range_DPS": phy_range,
        "Magic_melee_DPS": magic_melee,
        "Magic_range_DPS": magic_range,
        "Magic_resist": magic_resist,
        "Physical_resist": physical_resist
    }


# ==========================================================
# 4. ФУНКЦІЯ С *ARGS
# ==========================================================

def calculate_team_power(*team):

    total = 0

    for character in team:
        total += calculate_power(character)

    return round(total, 2)


# ==========================================================
# 5. РЕКУРСИВНА ФУНКЦІЯ
# ==========================================================

def recursive_best_team(data, size, index=0, team=None):

    if team is None:
        team = []

    # 1 базовий випадок
    if len(team) == size:
        return team, calculate_team_power(*team)

    #2 базовий випадок
    if index >= len(data):
        return [], -1

    team1, power1 = recursive_best_team(
        data,
        size,
        index + 1,
        team + [data[index]]
    )

    team2, power2 = recursive_best_team(
        data,
        size,
        index + 1,
        team
    )

    if power1 >= power2:
        return team1, power1

    return team2, power2

# ==========================================================
# 6. ФУНКЦІЯ ВИЩОГО ПОРЯДКУ
# ==========================================================

def process_data(data, operation):

    result = []

    for item in data:
        result.append(operation(item))

    return result

# ==========================================================
# 7. ПОШУК ПЕРСОНАЖА
# ==========================================================

def find_character(name):

    for character in characters:

        if character["Name"].lower() == name.strip().lower():
            return character

    return None

# ==========================================================
# ДВІ LAMBDA-ФУНКЦІЇ
# ==========================================================

get_physical = lambda c: (
    c["Phy_melee_DPS"] + c["Phy_range_DPS"]
)

get_magic = lambda c: (
    c["Magic_melee_DPS"] + c["Magic_range_DPS"]
)

get_physical.__doc__ = "Вертає фіз DPS."
get_magic.__doc__ = "Вертає маг DPS."


# ==========================================================
# ОСНОВНА ПРОГРАМА
# ==========================================================

while True:

    print("\n======================================")
    print("        RPG CHARACTER ANALYZER")
    print("======================================")
    print("1. Показати всіх персонажів")
    print("2. Знайти персонажа")
    print("3. Додати нового персонажа")
    print("4. Знайти персонажа за уроном")
    print("5. Показати найсильніших персонажів")
    print("6. Розрахувати силу команди")
    print("7. Статистика персонажів")
    print("8. Рекурсивно підібрати команду")
    print("0. Вихід")
    print("======================================")

    try:
        choice = int(input("Ваш вибір: "))

    except ValueError:
        print("Помилка! Введіть число.")
        continue

    # ======================================================
    # 1. ПОКАЗАТИ ВСІХ ПЕРСОНАЖЕЙ
    # ======================================================

    if choice == 1:

        for c in characters:

            print("\n------------------------------")

            print("Name:", c["Name"])
            print("Level:", c["Level"])
            print("Health:", c["Health"])

            print(
                "Physical melee DPS:",
                c["Phy_melee_DPS"]
            )

            print(
                "Physical ranged DPS:",
                c["Phy_range_DPS"]
            )

            print(
                "Magic melee DPS:",
                c["Magic_melee_DPS"]
            )

            print(
                "Magic ranged DPS:",
                c["Magic_range_DPS"]
            )

            print(
                "Magic resistance:",
                c["Magic_resist"]
            )

            print(
                "Physical resistance:",
                c["Physical_resist"]
            )

            print("Total DPS:", calculate_damage(c))
            print("Combat power:", calculate_power(c))


    # ======================================================
    # 2. ЗНАЙТИ ПЕРСОНАЖА
    # ======================================================

    elif choice == 2:

        name = input(
            "Введіть ім'я на англійській мові: "
        )

        c = find_character(name)

        if c is None:
            print("Персонаж не знайден.")

        else:

            print("\n------------------------------")

            print("Name:", c["Name"])
            print("Level:", c["Level"])
            print("Health:", c["Health"])

            print(
                "Physical melee DPS:",
                c["Phy_melee_DPS"]
            )

            print(
                "Physical ranged DPS:",
                c["Phy_range_DPS"]
            )

            print(
                "Magic melee DPS:",
                c["Magic_melee_DPS"]
            )

            print(
                "Magic ranged DPS:",
                c["Magic_range_DPS"]
            )

            print(
                "Magic resistance:",
                c["Magic_resist"]
            )

            print(
                "Physical resistance:",
                c["Physical_resist"]
            )

            print("Total DPS:", calculate_damage(c))
            print("Combat power:", calculate_power(c))


    # ======================================================
    # 3. ДОДАТИ ПЕРСОНАЖА
    # ======================================================

    elif choice == 3:

        name = input(
            "Введіть ім'я новового персонажа: "
        ).strip()

        if not name:
            print("Ім'я не може бути пустим.")
            continue

        if find_character(name) is not None:
            print("Такий персонаж вже є.")
            continue

        try:

            level = int(input("Level: "))
            health = int(input("Health: "))

            phy_melee = int(
                input("Physical melee DPS: ")
            )

            phy_range = int(
                input("Physical ranged DPS: ")
            )

            magic_melee = int(
                input("Magic melee DPS: ")
            )

            magic_range = int(
                input("Magic ranged DPS: ")
            )

            magic_resist = int(
                input("Magic resistance: ")
            )

            physical_resist = int(
                input("Physical resistance: ")
            )

        except ValueError:

            print("Помилка! Введіть цілі числа.")
            continue


        # Проверка введенных данных

        if level <= 0:
            print("Рівень повинен бути вище 0.")
            continue

        if health <= 0:
            print("Здоров'є повинно бути вище 0.")
            continue

        values = [
            phy_melee,
            phy_range,
            magic_melee,
            magic_range,
            magic_resist,
            physical_resist
        ]

        if any(value < 0 for value in values):

            print(
                "Урон та резіст не можуть "
                "бути від'ємними."
            )

            continue

        new_character = create_character(
            name,
            level,
            health,
            phy_melee,
            phy_range,
            magic_melee,
            magic_range,
            magic_resist,
            physical_resist
        )

        characters.append(new_character)

        print("\nПерсонаж успішно додан!")


    # ======================================================
    # 4. ПОШУК ПО УРОНУ
    # ======================================================

    elif choice == 4:

        print("\nВибрати тип урона:")
        print("1. Physical DPS")
        print("2. Magic DPS")

        try:

            attack = int(input("Ваш вибір: "))

            if attack not in (1, 2):
                print("Невірний тип.")
                continue

            minimum = int(
                input("Введіть мінімальний DPS: ")
            )

            if minimum < 0:
                print("DPS не може бути від'ємним.")
                continue

        except ValueError:

            print("Помилка! Введіть число.")
            continue


        if attack == 1:
            operation = get_physical

        else:
            operation = get_magic


        result = list(
            filter(
                lambda c: operation(c) >= minimum,
                characters
            )
        )


        if not result:

            print("Таких персонажів нема.")

        else:

            print("\nЗнайдені персонажі:")

            for c in result:

                print(
                    c["Name"],
                    "-",
                    operation(c),
                    "DPS"
                )


    # ======================================================
    # 5. НАЙСИЛЬНІШІ ПЕРСОНАЖІ
    # ======================================================

    elif choice == 5:

        sorted_characters = sorted(
            characters,
            key=calculate_power,
            reverse=True
        )

        print("\nТОП-5 ЗА БОЙОВОЮ СИЛОЮ:")

        for c in sorted_characters[:5]:

            print(
                c["Name"],
                "-",
                calculate_power(c)
            )


    # ======================================================
    # 6. РОЗРАХУВАТИ СИЛУ КОМАНДИ
    # ======================================================

    elif choice == 6:

        try:

            count = int(
                input(
                    "Скільки персонажів в команді? "
                )
            )

            if count < 1 or count > len(characters):

                print("Невірна кількість.")
                continue

        except ValueError:

            print("Помилка!Введіть ціле число.")
            continue


        team = []
        used_names = set()

        for i in range(count):

            name = input(
                f"Ім'я персонажа {i + 1}: "
            )

            c = find_character(name)

            if c is None:

                print("Персонаж не знайден.")
                break

            if c["Name"] in used_names:

                print("Цей персонаж вже у команді.")
                break

            team.append(c)
            used_names.add(c["Name"])


        if len(team) == count:

            total = calculate_team_power(*team)

            print("\nСклад команди:")

            for c in team:
                print("-", c["Name"])

            print(
                "\nЗагальна бойова сила:",
                total
            )


    # ======================================================
    # 7. СТАТИСТИКА ПЕРСОНАЖІВ
    # ======================================================

    elif choice == 7:

        print("\n========== СТАТИСТИКА ==========")


        physical = list(
            map(get_physical, characters)
        )

        magic = list(
            map(get_magic, characters)
        )


        total_physical = reduce(
            lambda x, y: x + y,
            physical,
            0
        )

        total_magic = reduce(
            lambda x, y: x + y,
            magic,
            0
        )


        powers = process_data(
            characters,
            calculate_power
        )


        damage_data = physical + magic


        print(
            "Кількість персонажів:",
            len(characters)
        )

        print(
            "Кількість значень DPS:",
            len(damage_data)
        )

        print(
            "Загальний фіз DPS:",
            total_physical
        )

        print(
            "Загальний маг DPS:",
            total_magic
        )

        print(
            "Середній DPS:",
            round(
                sum(damage_data) / len(damage_data),
                2
            )
        )

        print(
            "Средня бойова сила:",
            round(
                sum(powers) / len(powers),
                2
            )
        )

        print(
            "Максимальна бойова сила:",
            max(powers)
        )


    # ======================================================
    # 8. РЕКУРСИВНИЙ ПІДБІР КОМАНДИ
    # ======================================================

    elif choice == 8:

        try:

            size = int(
                input(
                    "Кількість персонажів у команді: "
                )
            )

            if size < 1 or size > len(characters):

                print("Невірна кількість.")
                continue

        except ValueError:

            print("Помилка!Введіть ціле число.")
            continue


        if len(characters) > 20:

            print(
                "Для рекурсивної добірки доступно "
                "не більше 20 персонажій."
            )

            continue

        best_team, power = recursive_best_team(
            characters,
            size
        )


        print("\nПІДІБРАНА КОМАНДА:")

        for c in best_team:

            print(
                c["Name"],
                "- сила:",
                calculate_power(c)
            )

        print(
            "\nЗагальна сила:",
            power
        )

    # ======================================================
    # 0. ВИХІД
    # ======================================================

    elif choice == 0:

        print("\nПрограма завершена.")
        break

    else:
        print(
            "Помилка!Виберіть пункт від 0 до 8."
        )
