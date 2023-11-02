def solution():
    points_per_round = 10
    total_points = 60
    points_lost = 20

    # Calculate the total number of points Jane earned
    total_points_earned = total_points + points_lost

    # Calculate the total number of rounds Jane played
    num_rounds = total_points_earned / points_per_round
    result = num_rounds
    return result

print(solution())