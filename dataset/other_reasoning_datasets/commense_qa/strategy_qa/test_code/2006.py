def solution():
    vegetarian_diet = ["meat", "fish", "poultry"]
    meat_free_items = ["hash browns", "waffle fries", "superfood sides"]
    overlap = [item for item in vegetarian_diet if item in meat_free_items]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())