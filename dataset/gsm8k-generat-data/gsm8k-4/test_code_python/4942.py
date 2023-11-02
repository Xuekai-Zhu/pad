def solution():
    """The Lady Eagles basketball team scored a total of 311 points in 5 games. Some players combined for 188 points. Lisa, Jessie, and Devin equally scored the rest. How many points did Jessie score?"""
    # Define the total number of points and the number of points scored by some players
    total_points = 311
    some_players_points = 188

    # Calculate the remaining number of points
    remaining_points = total_points - some_players_points

    # Divide the remaining points equally among Lisa, Jessie, and Devin
    each_player_points = remaining_points / 3

    # Calculate the number of points scored by Jessie
    jessie_points = each_player_points

    result = jessie_points
    return result

print(solution())