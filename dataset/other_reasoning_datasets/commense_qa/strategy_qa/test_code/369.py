def solution():
    # Define the ingredients in French toast and the fact that goat milk can be used in foods sold in supermarkets
    french_toast_ingredients = ["bread", "eggs", "milk", "cinnamon"]
    goat_milk_used_in_supermarkets = True
    # Check if goat milk can be used as an ingredient in French toast
    if goat_milk_used_in_supermarkets and "milk" in french_toast_ingredients:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())