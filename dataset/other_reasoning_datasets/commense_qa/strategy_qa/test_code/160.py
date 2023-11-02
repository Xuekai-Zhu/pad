def solution():
    horchata_ingredients = ["dry rice", "water", "spices", "sweetener"]
    rice_pudding_ingredients = ["cooked rice", "eggs", "milk", "sugar"]
    # Check if adding water to rice pudding creates all the ingredients of horchata
    if set(horchata_ingredients).issubset(set(rice_pudding_ingredients)):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())