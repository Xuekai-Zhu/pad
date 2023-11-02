def solution():
    
    total_milk = 16
    kids_consumption = total_milk * 0.75
    remaining_milk = total_milk - kids_consumption
    cooking_milk = remaining_milk * 0.5
    leftover_milk = remaining_milk - cooking_milk
    result = leftover_milk

    return result

print(solution())