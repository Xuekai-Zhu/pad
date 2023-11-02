def solution():
    """Jenny likes to play board games with her friends. She likes to play against her friend Mark the most, as she's played him 10 times and Mark has only won once. She doesn't like playing Jill, as she's played her twice as many times as she's played Mark and Jill has won 75% of them. How many times in total has Jenny won board games with her two friends?"""
    mark_plays = 10
    mark_wins = 1
    jill_plays = 2 * mark_plays
    jill_wins = int(0.75 * jill_plays)
    jenny_wins = (mark_plays - mark_wins) + (jill_plays - jill_wins)
    result = jenny_wins
    return result

print(solution())