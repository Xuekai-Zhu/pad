def solution():
    non-liquid ingredients = ["meatballs", "pasta", "chicken", "noodles"]
    liquid_diet = True
    if liquid_diet and any(ingredient in non-liquid ingredients for ingredient in soup):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())