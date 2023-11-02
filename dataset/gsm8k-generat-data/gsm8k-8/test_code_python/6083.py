def solution():
    # Calculate the current average of all rolls
    rolls = [1, 3, 2, 4, 3, 5, 3, 4, 4, 2]
    current_average = sum(rolls) / len(rolls)

    # Calculate the sum of all rolls so far
    sum_of_rolls = sum(rolls)

    # Calculate the number of rolls needed to average to 3
    needed_rolls = ((len(rolls) + 1) * 3) - sum_of_rolls

    # Calculate what Ronald needs to roll on the next roll
    needed_roll = int((needed_rolls - (current_average * len(rolls))) / (len(rolls) + 1))

    result = needed_roll
    return result

print(solution())