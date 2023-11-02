def solution():
    """The owner of a small store divided the sugar into 12 packs. If each pack weighs 250 grams and has 20 grams of sugar left, how many grams of sugar did he start with?"""
    # Define the weight of each pack and the amount of sugar left in each pack
    pack_weight = 250
    sugar_left = 20

    # Calculate the total weight of sugar left
    total_sugar_left = sugar_left * 12

    # Calculate the total weight of sugar initially
    total_sugar = (12 * pack_weight) + total_sugar_left

    # return the result
    result = total_sugar
    return result

print(solution())