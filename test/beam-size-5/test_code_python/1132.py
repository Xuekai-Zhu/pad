def solution():
    # Calculate the total number of marbles Bob will have after receiving 2 dozen more
    total_marbles = 60 + (2 * 12)  # Bob receives 2 dozen more marbles than he will have 60 marbles

    # Calculate the number of marbles Bob will have after losing 10
    remaining_marbles = total_marbles - 10

    result = remaining_marbles
    return result

print(solution())