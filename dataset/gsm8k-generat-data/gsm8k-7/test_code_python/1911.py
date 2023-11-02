def solution():
    brooke_balloons = 12
    tracy_balloons = 6

    # Add 8 balloons to Brooke's current total
    brooke_balloons += 8

    # Add 24 balloons to Tracy's current total
    tracy_balloons += 24

    # Calculate how many balloons Tracy will have after popping half
    tracy_balloons_after_pop = tracy_balloons / 2

    # Calculate the total number of balloons
    total_balloons = brooke_balloons + tracy_balloons_after_pop

    result = total_balloons
    return result

print(solution())