def solution():
    
    total_people = 30 + 45
    pizza_eaters = (2/3) * 30 + (4/5) * 45
    non_pizza_eaters = total_people - pizza_eaters
    result = non_pizza_eaters
    return result

print(solution())