def solution():
    hawaiian_cuisine = ["Spam", "Kalua pig", "fish", "seafood"]
    vegan_friendly = ["vegetables", "fruits", "grains", "legumes"]
    overlap = [food for food in hawaiian_cuisine if food in vegan_friendly]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())