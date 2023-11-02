def solution():
    # Calculate the total points made from 2-point shots
    total_2pt_shots = 7
    points_from_2pt = total_2pt_shots * 2

    # Calculate the total points made from 3-point shots
    total_3pt_shots = 3
    points_from_3pt = total_3pt_shots * 3

    # Calculate the total points made
    total_points = points_from_2pt + points_from_3pt
    result = total_points
    return result

print(solution())