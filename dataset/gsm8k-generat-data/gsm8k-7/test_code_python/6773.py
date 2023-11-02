def solution():
    num_nights_so_far = 4
    total_tips_so_far = 20 + 60 + 15 + 40
    desired_average_tips_per_night = 50
    num_nights_left = 1  # Jerry wants to know how much he needs to earn tonight

    # Calculate the total tips Jerry wants to earn
    total_desired_tips = (num_nights_so_far + num_nights_left) * desired_average_tips_per_night

    # Calculate how much Jerry needs to earn tonight
    desired_tips_tonight = total_desired_tips - total_tips_so_far

    result = desired_tips_tonight
    return result

print(solution())