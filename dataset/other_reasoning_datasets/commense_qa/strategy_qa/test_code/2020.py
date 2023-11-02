def solution():
    italian_restaurant = "Carmine's"
    essential_ingredient = "basil"
    # Check if the essential ingredient is missing
    if essential_ingredient not in italian_restaurant:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())