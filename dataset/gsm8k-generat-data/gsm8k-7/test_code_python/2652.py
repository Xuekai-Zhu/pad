def solution():
    num_family1 = 3
    donation1 = 10
    num_family2 = 15
    donation2 = 5
    goal = 150

    # Calculate total donation from family 1
    total_family1 = num_family1 * donation1

    # Calculate total donation from family 2
    total_family2 = num_family2 * donation2

    # Calculate total donation so far
    total_donation = total_family1 + total_family2

    # Calculate how much more they need to reach their goal
    remaining_goal = goal - total_donation
    result = remaining_goal
    return result

print(solution())