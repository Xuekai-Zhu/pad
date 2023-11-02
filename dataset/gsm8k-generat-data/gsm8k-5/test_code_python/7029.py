def solution():
    initial_marbles = 26  # Hilton started with 26 marbles
    found_marbles = 6  # Hilton found 6 marbles while playing
    lost_marbles = 10  # Hilton lost 10 marbles after playing
    lori_marbles = 2 * lost_marbles  # Lori gave Hilton twice the number of marbles he lost

    # Calculate the total number of marbles Hilton had in the end
    total_marbles = initial_marbles + found_marbles - lost_marbles + lori_marbles
    result = total_marbles
    return result

print(solution())