def solution():
    carmines_restaurant_type = "Italian"
    essential_ingredient = "olive oil"
    if carmines_restaurant_type == "Italian" and essential_ingredient not in carmines_kitchen:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())