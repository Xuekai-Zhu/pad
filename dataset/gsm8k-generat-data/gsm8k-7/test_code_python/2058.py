def solution():
    tobee_points = 4
    jay_points = tobee_points + 6
    sean_points = (tobee_points + jay_points) - 2

    # Calculate the total points of the team
    total_points = tobee_points + jay_points + sean_points
    result = total_points
    return result

print(solution())