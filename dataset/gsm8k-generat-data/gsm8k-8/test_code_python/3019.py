def solution():
    # Define the initial number of green marbles
    green_marbles = 26

    # Calculate the total number of blue marbles after buying the bags
    total_blue_marbles = 6 * 10

    # Calculate the total number of marbles before giving the gift
    total_marbles = green_marbles + total_blue_marbles

    # Subtract the marbles in the gift to get the new total
    new_total = total_marbles - (6 + 8)

    result = new_total
    return result

print(solution())