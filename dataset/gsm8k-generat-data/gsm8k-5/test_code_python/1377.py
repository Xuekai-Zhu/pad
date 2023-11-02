def solution():
    # Adelaide bought 30 ducks
    adelaide_ducks = 30

    # Ephraim bought 45 fewer ducks than Kolton
    kolton_ducks = (adelaide_ducks / 2) + 45
    ephraim_ducks = kolton_ducks - 45

    # Calculate the total number of ducks bought by the three students
    total_ducks = adelaide_ducks + ephraim_ducks + kolton_ducks

    # Calculate the average number of ducks bought by the three students
    average_ducks = total_ducks / 3
    result = average_ducks
    return result

print(solution())