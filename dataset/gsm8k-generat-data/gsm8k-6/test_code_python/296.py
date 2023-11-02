def solution():
    # Calculate the amount of sugar in each bag
    sugar_per_bag = 24 / 4  

    # Calculate how much sugar is lost due to the torn bag
    lost_sugar = sugar_per_bag / 2  

    # Calculate how much sugar remains
    remaining_sugar = (sugar_per_bag - lost_sugar) * 3  

    result = remaining_sugar
    return result

print(solution())