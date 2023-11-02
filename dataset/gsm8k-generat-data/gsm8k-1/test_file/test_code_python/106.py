def solution():
    """Marcell and Beatrice are having a contest to see who can eat the most fruit roll-ups, so they unroll as many as they can find. Unfortunately, someone makes a mistake and Beatrice's was two roll-ups wide and 24 rolls up long while Marcell's was 3 roll-ups wide and 14 roll-ups long. If they both ate their entire amount, how many did they eat on average?"""
    beatrice_rollups = 2 * 24
    marcell_rollups = 3 * 14
    total_rollups = beatrice_rollups + marcell_rollups
    average_rollups = total_rollups / 2
    result = average_rollups
    return result

print(solution())