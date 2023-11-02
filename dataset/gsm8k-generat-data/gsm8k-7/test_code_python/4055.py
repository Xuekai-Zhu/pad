def solution():
    num_clowns = 4
    num_children = 30
    total_riders = num_clowns + num_children
    initial_candy_count = 700
    candies_sold_per_rider = 20

    # Calculate the total number of candies sold
    total_candies_sold = total_riders * candies_sold_per_rider

    # Calculate the number of candies left
    candies_left = initial_candy_count - total_candies_sold
    result = candies_left
    return result

print(solution())