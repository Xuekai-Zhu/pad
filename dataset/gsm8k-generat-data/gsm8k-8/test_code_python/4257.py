def solution():
    burgers_per_day = 3
    calories_per_burger = 20
    days = 2

    total_burgers = burgers_per_day * days
    total_calories = total_burgers * calories_per_burger
    result = total_calories
    return result

print(solution())