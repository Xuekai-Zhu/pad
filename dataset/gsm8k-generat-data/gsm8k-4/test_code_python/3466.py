def solution():
    """UF got into the national championship. For them to get into the championship, they scored a total of 720 points during their previous 24 games. In the championship game, however, their opponent was much stronger than any other team they had previously gone against and they scored 2 points less than half as much as they had previously scored in each of the 24 games. Their opponent only lost by 2 points. How many points did their opponent score?"""
    # Calculate the total points UF scored in their previous 24 games
    uf_points = 720

    # Calculate the average points UF scored in each of the previous 24 games
    uf_average = uf_points / 24

    # Calculate the number of points UF's opponent scored in the championship game
    opponent_points = (uf_average / 2) - 2

    # Add the two points UF's opponent lost by to get the total points scored by the opponent
    total_opponent_points = opponent_points + 2

    result = total_opponent_points
    return result

print(solution())