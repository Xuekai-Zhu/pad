def solution():
    """A herring has 40 oz of fat, an eel 20 oz, and a pike 10 more oz of fat than an eel. If Ellianna cooked and served 40 fish of each type, calculate how many ounces of fat she served."""
    herring_fat = 40
    eel_fat = 20
    pike_fat = eel_fat + 10
    fish_per_type = 40
    total_fat_served = (herring_fat + eel_fat + pike_fat) * fish_per_type
    result = total_fat_served
    return result

print(solution())