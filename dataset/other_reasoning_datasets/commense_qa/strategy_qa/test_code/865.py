def solution():
    british_breakfast_items = ["baked beans", "toast", "grilled vegetables"]
    us_dinner_items = ["barbecue", "grilled mushrooms", "grilled tomatoes"]
    if "baked beans" in british_breakfast_items and "grilled mushrooms" in us_dinner_items:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())