def solution():
    # Finding the number of ducks bought by Ephraim and Kolton
    ephraim_ducks = 30 / 2  # Adelaide bought twice the number of ducks Ephraim bought
    kolton_ducks = ephraim_ducks + 45  # Ephraim bought 45 fewer ducks than Kolton

    # Finding the total number of ducks and the average number
    total_ducks = 30 + ephraim_ducks + kolton_ducks
    average_ducks = total_ducks / 3

    result = average_ducks
    return result

print(solution())