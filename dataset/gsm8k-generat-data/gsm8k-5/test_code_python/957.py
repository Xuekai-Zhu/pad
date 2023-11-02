def solution():
    coals_per_time = 15/20  # The grill burns 15 coals every 20 minutes
    coals_per_bag = 60  # Each bag of coal contains 60 coals
    total_coals = 3 * coals_per_bag  # The grill burned 3 bags of coal

    # Calculate the total time the grill ran in minutes
    total_time = total_coals / coals_per_time

    # Convert the total time to hours and minutes
    hours = int(total_time / 60)
    minutes = int(total_time % 60)
    result = f"{hours} hours and {minutes} minutes"
    return result

print(solution())