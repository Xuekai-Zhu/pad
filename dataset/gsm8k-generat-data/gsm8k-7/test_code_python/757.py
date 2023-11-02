def solution():
    daily_kibble = 2
    bag_capacity = 12

    # Calculate the total amount of kibble that Luna ate in one day
    total_kibble_eaten = 1 + 1 + 1 + (2 * 1)

    # Calculate the amount of kibble left in the bag
    kibble_left = bag_capacity - total_kibble_eaten
    result = kibble_left
    return result

print(solution())