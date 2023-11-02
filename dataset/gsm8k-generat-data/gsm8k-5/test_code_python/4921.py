def solution():
    # Calculate the total amount of money in dollars and cents
    dollars = 2 + 5 + (13 * 0.25) + (20 * 0.10) + (8 * 0.05) + (35 * 0.01)
    cents = int(round((dollars - int(dollars)) * 100))

    # Format the output as a string
    result = "${}.{:02}".format(int(dollars), cents)
    return result

print(solution())