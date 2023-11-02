def solution():
    vegan_consumption = "no animals or animal products"
    paella_ingredients = ["rabbit", "chicken"]
    contains_animal_products = any(ingredient in paella_ingredients for ingredient in vegan_consumption.split())
    if contains_animal_products:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())