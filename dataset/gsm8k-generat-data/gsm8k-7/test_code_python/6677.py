def solution():
    num_classmates = 30
    time_to_find_flower = 10
    total_time = 2 * 60  # 2 hours in minutes
    lost_flowers = 3

    # Calculate the total number of flowers he needs to gather
    total_flowers_needed = num_classmates

    # Calculate the total time he has spent gathering flowers, taking into account the lost flowers
    total_time_spent = total_time - (lost_flowers * time_to_find_flower)

    # Calculate the time he still needs to spend gathering flowers
    remaining_time = (total_flowers_needed * time_to_find_flower) - total_time_spent
    result = remaining_time
    return result

print(solution())