def solution():
    remaining_marbles = 20

    # Calculate the number of marbles Archie had before losing 60% on the street
    initial_marbles = remaining_marbles / (1 - 0.6)

    # Calculate the number of marbles Archie had remaining after losing half of them down a sewer
    remaining_marbles = initial_marbles / 2

    result = remaining_marbles
    return result

print(solution())