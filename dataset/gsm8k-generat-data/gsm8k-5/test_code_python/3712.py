def solution():
    bags_per_time = 3  # Peter rakes 3 bags of leaves in 15 minutes
    time_per_bags = 15  # Peter takes 15 minutes to rake 3 bags of leaves

    # Calculate the time Peter will take to rake 8 bags of leaves
    total_time = (8 / bags_per_time) * time_per_bags
    result = total_time
    return result

print(solution())