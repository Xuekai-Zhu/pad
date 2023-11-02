def solution():
    # Calculate the total number of candy bars Kim's dad bought in 16 weeks
    total_bars_bought = 2 * 16

    # Calculate the number of candy bars Kim ate in 16 weeks
    bars_eaten = 16 / 4

    # Calculate the number of candy bars Kim saved in 16 weeks
    bars_saved = total_bars_bought - bars_eaten

    result = bars_saved
    return result

print(solution())