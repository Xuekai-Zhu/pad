def solution():
    elizabeth_I_life_span = [1533, 1603]
    dido_play_written = [1587, 1593]
    if elizabeth_I_life_span[0] <= dido_play_written[1] and elizabeth_I_life_span[1] >= dido_play_written[0]:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())