def solution():
    
    cup_size = 12
    first_drink = cup_size / 4
    second_drink = cup_size / 2
    remaining_coffee = cup_size - first_drink - second_drink
    final_drink = 1
    remaining_coffee -= final_drink

    result = remaining_coffee
    return result

print(solution())