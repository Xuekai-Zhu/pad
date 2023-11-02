def solution():
    """Taro and Vlad play a video game competition together, earning 5 points for every win. After playing 30 rounds, Taro scored 4 points less than 3/5 of the total points scored. How many total points did Vlad score?"""
    # Define the number of rounds and points per win
    ROUNDS = 30
    POINTS_PER_WIN = 5

    # Calculate the total points scored by both players in the 30 rounds
    total_points = ROUNDS * 2 * POINTS_PER_WIN

    # Calculate the points scored by Taro
    taro_points = (3/5) * total_points - 4

    # Calculate the points scored by Vlad
    vlad_points = total_points - taro_points

    # Return the result
    result = vlad_points
    return result

print(solution())