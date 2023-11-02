def solution():
    """For every muffin, Svetlana needed 5 tablespoons of flour, 3 tablespoons of sugar, and 0.25 of a tablespoon of salt. How many tablespoons of dry ingredients would Svetlana need to make 16 muffins?"""
    muffins = 16
    flour_per_muffin = 5
    sugar_per_muffin = 3
    salt_per_muffin = 0.25
    total_flour = muffins * flour_per_muffin
    total_sugar = muffins * sugar_per_muffin
    total_salt = muffins * salt_per_muffin
    total_dry_ingredients = total_flour + total_sugar + total_salt
    result = total_dry_ingredients
    return result

print(solution())