def solution():
    
    flour_per_muffin = 5
    sugar_per_muffin = 3
    salt_per_muffin = 0.25
    total_flour = flour_per_muffin * 16
    total_sugar = sugar_per_muffin * 16
    total_salt = salt_per_muffin * 16
    total_dry_ingredients = total_flour + total_sugar + total_salt
    result = total_dry_ingredients
    return result

print(solution())