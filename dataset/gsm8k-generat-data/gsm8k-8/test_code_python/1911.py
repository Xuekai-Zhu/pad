def solution():
    # Calculate Brooke's total balloons after adding 8
    brooke_total = 12 + 8

    # Calculate Tracy's balloons after adding 24
    tracy_total = 6 + 24

    # Calculate how many balloons Tracy has left after popping half
    tracy_left = tracy_total / 2

    # Calculate the total balloons between both of them
    total_balloons = brooke_total + tracy_left
    result = total_balloons
    return result

print(solution())