def solution():
    # Calculate the number of oranges Johann has after eating 10
    remaining_oranges = 60 - 10  # Johann ate 10 oranges
    stolen_oranges = remaining_oranges / 2  # Half of the remaining oranges were stolen by Carson
    remaining_oranges = remaining_oranges - stolen_oranges + 5  # Carson returned 5 oranges
    result = remaining_oranges
    return result

print(solution())