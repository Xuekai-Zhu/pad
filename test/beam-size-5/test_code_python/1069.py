def solution():
    
    total_bananas = 315
    first_monkey_bananas = 10
    second_monkey_bananas = first_monkey_bananas + 4
    third_monkey_bananas = total_bananas - first_monkey_bananas - second_monkey_bananas
    result = third_monkey_bananas
    return result

print(solution())