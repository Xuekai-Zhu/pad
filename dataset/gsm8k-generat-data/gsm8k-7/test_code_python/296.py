def solution():
    total_sugar = 24
    num_bags = 4
    sugar_per_bag = total_sugar / num_bags

    # Calculate the amount of sugar lost when one bag gets torn
    lost_sugar = sugar_per_bag / 2

    # Calculate the remaining amount of sugar
    remaining_sugar = total_sugar - lost_sugar
    result = remaining_sugar
    return result

print(solution())