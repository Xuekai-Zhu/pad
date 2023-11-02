def solution():
    # Calculate the number of clear marbles Percius has
    clear_marbles = 0.4 * total_marbles

    # Calculate the number of black marbles Percius has
    black_marbles = 0.2 * total_marbles

    # Calculate the number of marbles of other colors Percius has
    other_marbles = total_marbles - clear_marbles - black_marbles

    # Calculate the average number of marbles of other colors his friend will get
    avg_other_marbles = (other_marbles / total_marbles) * 5
    result = avg_other_marbles
    return result

print(solution())