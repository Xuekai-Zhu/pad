def solution():
    flour_per_muffin = 5
    sugar_per_muffin = 3
    salt_per_muffin = 0.25
    num_muffins = 16

    # Calculate the total tablespoons of flour needed for 16 muffins
    total_flour = flour_per_muffin * num_muffins

    # Calculate the total tablespoons of sugar needed for 16 muffins
    total_sugar = sugar_per_muffin * num_muffins

    # Calculate the total tablespoons of salt needed for 16 muffins
    total_salt = salt_per_muffin * num_muffins

    # Calculate the total tablespoons of dry ingredients needed
    total_dry_ingredients = total_flour + total_sugar + total_salt
    result = total_dry_ingredients
    return result

print(solution())