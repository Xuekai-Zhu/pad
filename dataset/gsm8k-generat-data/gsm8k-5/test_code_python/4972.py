def solution():
    initial_candy_bars = 7  # Amanda had 7 candy bars
    given_to_sister_1 = 3  # Amanda gave 3 candy bars to her sister the first time
    candy_bars_bought = 30  # Amanda won some prize money and bought 30 candy bars
    given_to_sister_2 = given_to_sister_1 * 4  # Amanda gave her sister 4 times as many candy bars the second time

    # Calculate the total number of candy bars Amanda has left
    total_candy_bars = initial_candy_bars + candy_bars_bought - given_to_sister_1 - given_to_sister_2
    result = total_candy_bars
    return result

print(solution())