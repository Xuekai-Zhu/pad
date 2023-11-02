def solution():
    num_trumpets = 10 - 3
    num_guitars = 2 * 2
    num_trombones = 1 + 2
    num_french_horns = num_guitars - 1

    # Calculate the total number of musical instruments
    total_instruments = num_trumpets + num_guitars + num_trombones + num_french_horns
    result = total_instruments
    return result

print(solution())