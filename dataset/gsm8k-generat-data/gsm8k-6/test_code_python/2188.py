def solution():
    # Calculate the total weight of the first two antacids
    weight_first_two = 2 * 2  # each antacid weighs 2 grams

    # Calculate the total weight of the three smaller antacids
    weight_next_three = 3 * 1  # each antacid weighs 1 gram

    # Calculate the total weight of all the antacids
    total_weight = weight_first_two + weight_next_three

    # Calculate the total amount of zinc in the first two antacids
    zinc_first_two = 0.05 * (2 * 2)  # each antacid weighs 2 grams and is 5% zinc by weight

    # Calculate the total amount of zinc in the three smaller antacids
    zinc_next_three = 0.15 * (3 * 1)  # each smaller antacid weighs 1 gram and is 15% zinc by weight

    # Calculate the total amount of zinc in all the antacids
    total_zinc = zinc_first_two + zinc_next_three

    # Convert the total amount of zinc to milligrams
    total_zinc_mg = total_zinc * 1000

    result = total_zinc_mg
    return result

print(solution())