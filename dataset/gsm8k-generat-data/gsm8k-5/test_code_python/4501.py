def solution():
    # Calculate the points scored by Roosevelt High School in each game
    first_game_points = 30
    second_game_points = first_game_points / 2
    third_game_points = second_game_points * 3

    # Calculate the total points scored by Roosevelt High School in the tournament
    total_points_Roosevelt = first_game_points + second_game_points + third_game_points + 50

    # Calculate the points scored by Greendale High School
    total_points_Greendale = total_points_Roosevelt - 10

    result = total_points_Greendale
    return result

print(solution())