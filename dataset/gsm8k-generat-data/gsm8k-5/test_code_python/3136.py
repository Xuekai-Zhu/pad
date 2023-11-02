def solution():
    # Define the cost and number of balloons per bag
    small_cost = 4
    small_balloons = 50
    medium_cost = 6
    medium_balloons = 75
    large_cost = 12
    large_balloons = 200

    # Define the total amount of money Mark has to spend
    total_money = 24

    # Calculate the maximum number of each type of bag that Mark can buy
    max_small_bags = total_money // small_cost
    max_medium_bags = total_money // medium_cost
    max_large_bags = total_money // large_cost

    # Calculate the maximum number of balloons Mark can buy with each type of bag
    max_small_balloons = max_small_bags * small_balloons
    max_medium_balloons = max_medium_bags * medium_balloons
    max_large_balloons = max_large_bags * large_balloons

    # Calculate the total number of balloons Mark can buy
    total_balloons = max(max_small_balloons, max_medium_balloons, max_large_balloons)

    result = total_balloons
    return result

print(solution())