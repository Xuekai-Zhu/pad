def solution():
    
    max_liquid = 32
    lunch_drink = 8
    recess_drink = 16
    total_drinks = lunch_drink + recess_drink
    remaining_liquid = max_liquid - total_drinks
    result = remaining_liquid
    return result

print(solution())