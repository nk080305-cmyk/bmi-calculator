def calculate_bmi(weight, height):
    """weight в кг, height в метрах"""
    bmi = weight / (height ** 2)
    return round(bmi, 1)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Недостаточный вес 📉"
    elif bmi < 25:
        return "Нормальный вес ✅"
    elif bmi < 30:
        return "Избыточный вес ⚠️"
    else:
        return "Ожирение 🚨"

# Использование
weight = float(input("Введи вес (кг): "))
height = float(input("Введи рост (м): "))

bmi = calculate_bmi(weight, height)
category = get_bmi_category(bmi)

print(f"\n📊 Твой ИМТ: {bmi}")
print(f"Статус: {category}")
