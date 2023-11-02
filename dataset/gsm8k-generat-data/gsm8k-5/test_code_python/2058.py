def solution():
    # Tobee scored 4 points
    tobee_points = 4

    # Jay scored 6 more than Tobee
    jay_points = tobee_points + 6

    # Tobee and Jay together scored (4 + 6) = 10 points
    # Sean scored 2 less than Tobee and Jay together
    sean_points = (tobee_points + jay_points) - 2

    # Total points scored by the team
    total_points = tobee_points + jay_points + sean_points
    result = total_points
    return result

print(solution())