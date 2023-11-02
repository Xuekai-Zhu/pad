def solution():
    """Dimitri eats 3 burgers per day. Each burger has a total of 20 calories. How many calories will he get after two days?"""
    burgers_per_day = 3
    calories_per_burger = 20
    days = 2
    total_calories = burgers_per_day * calories_per_burger * days
    result = total_calories
    return result

print(solution())