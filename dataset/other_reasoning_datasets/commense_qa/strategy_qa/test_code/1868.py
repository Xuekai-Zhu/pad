def solution():
    # Define the ingredients of lemonade and whether citrus fruit is high in Vitamin C
    lemonade_ingredients = ["lemons", "sugar", "water"]
    citrus_fruit_high_vit_c = True
    # Check if lemonade provides Vitamin C
    if "lemons" in lemonade_ingredients and citrus_fruit_high_vit_c:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())