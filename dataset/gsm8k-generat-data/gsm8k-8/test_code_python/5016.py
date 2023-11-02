def solution():
    # Define the total number of marbles
    total_marbles = 100

    # Calculate the number of clear and black marbles
    clear_marbles = 0.4 * total_marbles
    black_marbles = 0.2 * total_marbles

    # Calculate the number of marbles of other colors
    other_marbles = total_marbles - clear_marbles - black_marbles

    # Calculate the expected number of marbles of other colors the friend will get
    expected_other_marbles = (5 / total_marbles) * other_marbles
    result = expected_other_marbles
    return result

print(solution())