def solution():
    # Define the starting number of kids
    total_kids = 20

    # Calculate how many kids fall asleep in the first 5 minutes
    first_group = total_kids / 2

    # Calculate how many kids remain awake after the first 5 minutes
    remaining_kids = total_kids - first_group

    # Calculate how many of the remaining kids fall asleep in the next 5 minutes
    second_group = remaining_kids / 2

    # Calculate how many kids are still awake
    still_awake = remaining_kids - second_group

    result = still_awake
    return result

print(solution())