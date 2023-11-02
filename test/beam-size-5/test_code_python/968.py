def solution():
    # Calculate the total number of oranges Mrs. Harrington bought
    total_oranges = 12 * 20

    # Calculate the number of oranges Mrs. Harrington gave her mom and her sister
    given_oranges = 2 * 20

    # Calculate the number of oranges Mrs. Harrington kept
    kept_oranges = total_oranges / 4

    # Calculate the number of oranges Mrs. Harrington sold
    sold_oranges = total_oranges - given_oranges - kept_oranges

    result = sold_oranges
    return result

print(solution())