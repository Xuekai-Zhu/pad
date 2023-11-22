def solution():
    
    # Define the points scored in the first game
    game1_points = 14

    # Calculate the points scored in the second game
    game2_points = game1_points - 4

    # Calculate the points scored in the third game
    game3_points = game2_points - 6

    # Calculate the total points scored in both games
    total_points = game1_points + game2_points + game3_points

    # Display the total points scored
    result = total_points
    return result

print(solution())