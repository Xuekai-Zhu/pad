def solution():
    
    mark_plays = 10
    mark_wins = 1
    jill_plays = 2 * mark_plays
    jill_wins = int(0.75 * jill_plays)
    jenny_wins = (mark_plays - mark_wins) + (jill_plays - jill_wins)
    result = jenny_wins
    return result

print(solution())