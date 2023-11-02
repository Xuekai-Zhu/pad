def solution():
    sugar_per_pack = 250  # Each pack weighs 250 grams
    leftover_sugar_per_pack = 20  # There are 20 grams of sugar left in each pack
    total_leftover_sugar = leftover_sugar_per_pack * 12  # Calculate the total leftover sugar

    # Calculate the total amount of sugar
    total_sugar = sugar_per_pack * 12 + total_leftover_sugar
    result = total_sugar
    return result

print(solution())