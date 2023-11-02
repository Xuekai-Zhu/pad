def solution():
    breakfast_chocolate_milk = 8
    lunch_chocolate_milk = 8
    dinner_chocolate_milk = 8
    ending_chocolate_milk = 56
    total_chocolate_milk = ending_chocolate_milk + lunch_chocolate_milk + breakfast_chocolate_milk + dinner_chocolate_milk
    starting_chocolate_milk = total_chocolate_milk - 64
    result = starting_chocolate_milk
    return result

print(solution())