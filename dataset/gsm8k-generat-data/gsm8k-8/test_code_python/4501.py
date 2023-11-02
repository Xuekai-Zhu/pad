def solution():
    # Calculate the points scored by Roosevelt in each game
    game1_points = 30
    game2_points = 0.5 * game1_points
    game3_points = 3 * game2_points

    # Calculate the total points scored by Roosevelt
    total_points = game1_points + game2_points + game3_points

    # Add the bonus points to Roosevelt's total
    total_points += 50

    # Calculate the points scored by Greendale
    greendale_points = total_points - 10
    result = greendale_points
    return result

print(solution())