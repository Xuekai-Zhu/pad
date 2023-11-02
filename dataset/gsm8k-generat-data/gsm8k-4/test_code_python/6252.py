def solution():
    """Jenny likes to play board games with her friends. She likes to play against her friend Mark the most, as she's played him 10 times and Mark has only won once. She doesn't like playing Jill, as she's played her twice as many times as she's played Mark and Jill has won 75% of them. How many times in total has Jenny won board games with her two friends?"""
    # Define the number of times Jenny played Mark and the number of times Mark won
    mark_games = 10
    mark_wins = 1

    # Calculate the number of times Jenny played Jill and the number of times Jill won
    jill_games = mark_games * 2
    jill_wins = int(jill_games * 0.75)

    # Calculate the total number of times Jenny has won
    total_wins = (mark_games - mark_wins) + (jill_games - jill_wins)

    # return the result
    result = total_wins
    return result

print(solution())