def solution():
    garfield_favorites = ["spaghetti"]
    canid_favorites = ["meat", "dog food"]
    overlap = [food for food in garfield_favorites if food in canid_favorites]
    if overlap:
        result = "maybe"
    else:
        result = "no"
    return result

print(solution())