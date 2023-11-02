def solution():
    brooke_balloons = 12
    tracy_balloons = 6

    # Brooke adds 8 balloons to his current 12
    brooke_balloons += 8

    # Tracy adds 24 balloons to her current 6
    tracy_balloons += 24

    # Tracy pops half of her balloons
    tracy_balloons /= 2

    # Calculate the total number of balloons they have in total
    total_balloons = brooke_balloons + tracy_balloons
    result = total_balloons
    return result

print(solution())