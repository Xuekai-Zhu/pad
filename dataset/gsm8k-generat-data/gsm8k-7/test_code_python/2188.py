def solution():
    weight_of_big_antacid = 2 # grams
    zinc_percentage_of_big_antacid = 0.05 # or 5%
    weight_of_small_antacid = 1 # gram
    zinc_percentage_of_small_antacid = 0.15 # or 15%
    num_big_antacids = 2
    num_small_antacids = 3

    # Calculate the total weight of zinc in the big antacids
    zinc_in_big_antacids = weight_of_big_antacid * zinc_percentage_of_big_antacid * num_big_antacids

    # Calculate the total weight of zinc in the small antacids
    zinc_in_small_antacids = weight_of_small_antacid * zinc_percentage_of_small_antacid * num_small_antacids

    # Convert total zinc to milligrams
    total_zinc_mg = (zinc_in_big_antacids + zinc_in_small_antacids) * 1000
    result = total_zinc_mg
    return result

print(solution())