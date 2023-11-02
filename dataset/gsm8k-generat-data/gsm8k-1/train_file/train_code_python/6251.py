def solution():
    """Jenny likes to play board games with her friends. She likes to play against her friend Mark the most, as she's played him 10 times and Mark has only won once. She doesn't like playing Jill, as she's played her twice as many times as she's played Mark and Jill has won 75% of them. How many times in total has Jenny won board games with her two friends?"""
    mark_played = 10
    mark_won = 1
    jill_played = mark_played * 2
    jill_won = int(jill_played * 0.75)
    jenny_won = (mark_played - mark_won) + (jill_played - jill_won)
    result = jenny_won
    return result

print(solution())