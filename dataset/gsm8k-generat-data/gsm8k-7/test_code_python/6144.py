def solution():
    num_kids = 20

    # Calculate the number of kids who fall asleep in the first 5 minutes
    num_asleep_1 = num_kids // 2

    # Calculate the number of kids remaining after the first group falls asleep
    num_remaining_1 = num_kids - num_asleep_1

    # Calculate the number of kids who fall asleep in the second 5 minutes
    num_asleep_2 = num_remaining_1 // 2

    # Calculate the number of kids still awake
    num_awake = num_remaining_1 - num_asleep_2
    result = num_awake
    return result

print(solution())