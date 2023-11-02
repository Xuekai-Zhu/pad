def solution():
    # Calculate the points for the first-place team
    first_place_points = 12 * 2 + 4 * 1

    # Calculate the points for the second-place team
    second_place_points = 13 * 2 + 1 * 1

    # Calculate the points for Elsa's team
    elsa_points = 8 * 2 + 10 * 1

    # Sort the points in descending order
    points = sorted([first_place_points, second_place_points, elsa_points], reverse=True)

    # Calculate the average number of points for the playoff teams
    average_points = (points[0] + points[1] + points[2]) / 3

    result = average_points
    return result

print(solution())