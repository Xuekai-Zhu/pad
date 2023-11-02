def solution():
    """UF got into the national championship. For them to get into the championship, they scored a total of 720 points during their previous 24 games.  In the championship game, however, their opponent was much stronger than any other team they had previously gone against and they scored 2 points less than half as much as they had previously scored in each of the 24 games. Their opponent only lost by 2 points.  How many points did their opponent score?"""
    # Calculate the total points UF scored in the 24 previous games
    uf_points = 720

    # Calculate the average points scored by UF in each of the 24 previous games
    uf_avg = uf_points / 24

    # Calculate the points scored by UF's opponent in the championship game
    opponent_points = (uf_avg / 2) - 2

    # Calculate the total points scored by UF's opponent
    total_points = opponent_points + 2

    # Display the points scored by UF's opponent
    result = total_points
    return result

print(solution())