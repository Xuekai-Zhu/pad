def solution():
    """The Lady Eagles basketball team scored a total of 311 points in 5 games. Some players combined for 188 points. Lisa, Jessie, and Devin equally scored the rest. How many points did Jessie score?"""
    # Calculate the total points scored by Lisa, Jessie, and Devin
    points_ljd = 311 - 188

    # Divide the points equally among Lisa, Jessie, and Devin
    points_per_player = points_ljd / 3

    # Determine the number of points scored by Jessie
    points_jessie = points_per_player

    # Display the number of points Jessie scored
    result = points_jessie
    return result

print(solution())