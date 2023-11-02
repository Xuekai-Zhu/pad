def solution():
    # Define the number of kids on Lake Pleasant and the proportion who went tubing
    total_kids = 40
    tubing_proportion = 1/4

    # Calculate the number of kids who went tubing and the number of kids who went rafting
    tubing_kids = total_kids * tubing_proportion
    rafting_kids = tubing_kids * 1/2

    # Calculate the number of kids who did both activities
    both_activities = rafting_kids

    result = both_activities
    return result

print(solution())