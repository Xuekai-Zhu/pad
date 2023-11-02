def solution():
    # Define the total distance to run and the current distance run
    total_distance = 20
    current_distance = 2

    # Define the amount to add each week
    weekly_increase = 2/3

    # Calculate how many weeks it will take to reach the total distance
    weeks_to_train = (total_distance - current_distance) / weekly_increase
    result = weeks_to_train
    return result

print(solution())