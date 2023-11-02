def solution():
    bags_before_dinner = 1  # John eats 1 bag of chips for dinner
    bags_after_dinner = 2 * bags_before_dinner  # John eats twice as many after dinner

    # Calculate the total number of bags John eats
    total_bags = bags_before_dinner + bags_after_dinner
    result = total_bags
    return result

print(solution())