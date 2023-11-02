def solution():
    # Define the popular food items associated with Brooklyn
    brooklyn_foods = ["bagels", "pizza"]
    # Check if bread products are included in the list of popular Brooklyn foods
    if "bread" in brooklyn_foods:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())