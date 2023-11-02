def solution():
    menu_items = ["churros"]
    cinnamon_ingredients = ["cinnamon"]
    overlap = [ingredient for ingredient in cinnamon_ingredients if ingredient in menu_items]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())