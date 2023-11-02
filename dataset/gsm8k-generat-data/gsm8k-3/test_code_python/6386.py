def solution():
    """Nathan went to the arcade. He played the air hockey game 2 times and the basketball game 4 times. If each game cost 3 tokens, how many tokens did he use?"""
    # Define the number of times Nathan played each game
    AIR_HOCKEY_TIMES = 2
    BASKETBALL_TIMES = 4

    # Define the cost of each game in tokens
    GAME_COST = 3

    # Calculate the total number of tokens used by Nathan
    total_tokens = (AIR_HOCKEY_TIMES + BASKETBALL_TIMES) * GAME_COST

    # Display the total number of tokens used
    result = total_tokens
    return result

print(solution())