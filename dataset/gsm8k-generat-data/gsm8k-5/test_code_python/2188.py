def solution():
    # Calculate the weight of zinc in the larger antacids
    zinc_weight_big = 2 * 0.05  # Each big antacid has 5% zinc
    zinc_total_big = zinc_weight_big * 2  # Jerry takes 2 big antacids
    zinc_total_big_mg = zinc_total_big * 1000  # Convert to milligrams

    # Calculate the weight of zinc in the smaller antacids
    zinc_weight_small = 1 * 0.15  # Each small antacid has 15% zinc
    zinc_total_small = zinc_weight_small * 3  # Jerry takes 3 small antacids
    zinc_total_small_mg = zinc_total_small * 1000  # Convert to milligrams

    # Calculate the total amount of zinc Jerry eats
    total_zinc_mg = zinc_total_big_mg + zinc_total_small_mg
    result = total_zinc_mg
    return result

print(solution())