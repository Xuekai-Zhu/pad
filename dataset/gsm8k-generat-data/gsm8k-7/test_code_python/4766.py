def solution():
    bag_size = 24
    removal_rate = 4
    harvest_time = 3

    # Calculate the amount of sugar already harvested
    harvested_sugar = removal_rate * harvest_time

    # Calculate the amount of sugar remaining in the bag
    remaining_sugar = bag_size - harvested_sugar

    # Calculate how long it will take to harvest the remaining sugar
    remaining_time = remaining_sugar / removal_rate
    result = remaining_time
    return result

print(solution())