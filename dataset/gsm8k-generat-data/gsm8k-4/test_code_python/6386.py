def solution():
    """Nathan went to the arcade. He played the air hockey game 2 times and the basketball game 4 times. If each game cost 3 tokens, how many tokens did he use?"""
    # Define the number of times Nathan played each game
    air_hockey_times = 2
    basketball_times = 4

    # Define the cost of each game
    game_cost = 3

    # Calculate the total cost of all the games
    total_cost = (air_hockey_times + basketball_times) * game_cost

    result = total_cost
    return result

print(solution())