def solution():
    # Calculate the current average score per player for the first 9 rounds
    current_average = 10440 / (4 * 9)

    # Calculate the minimum average score per player needed to tie the record
    minimum_average = (287 * 10 - 10440) / 4

    # Calculate the difference between the minimum average and the current average
    difference = minimum_average - current_average
    result = difference
    return result

print(solution())