def solution():
    # Calculate the total number of oranges
    total_oranges = 10 * 30

    # Calculate the number of rotten oranges
    rotten_oranges = 50

    # Calculate the number of oranges for making juice
    juice_oranges = 30

    # Calculate the number of oranges to be sold
    sold_oranges = total_oranges - rotten_oranges - juice_oranges

    result = sold_oranges
    return result

print(solution())