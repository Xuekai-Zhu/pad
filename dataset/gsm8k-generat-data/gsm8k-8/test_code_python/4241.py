def solution():
    # Define the number of marbles each friend bought
    wolfgang_marbles = 16
    ludo_marbles = 1.25 * wolfgang_marbles
    michael_marbles = 2/3 * (wolfgang_marbles + ludo_marbles)

    # Calculate the total number of marbles
    total_marbles = wolfgang_marbles + ludo_marbles + michael_marbles

    # Calculate the number of marbles each friend gets
    each_gets = total_marbles / 3
    result = each_gets
    return result

print(solution())