def solution():
    initial_pick = 400
    subsequent_pick = (3/4) * initial_pick

    remaining_pick = 600

    target_pick = (initial_pick + subsequent_pick) * 2 + remaining_pick * 2
    result = target_pick
    return result

print(solution())