def solution():
    bags_per_time = 3
    time_per_bags = 15  # in minutes

    # Calculate the time it takes to rake one bag of leaves
    time_per_bag = time_per_bags / bags_per_time

    # Calculate the total time it will take to rake 8 bags of leaves
    total_time = time_per_bag * 8
    result = total_time
    return result

print(solution())