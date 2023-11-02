def solution():
    green_marbles = 26  # Janelle starts with 26 green marbles
    blue_marbles = 6 * 10  # Janelle buys 6 bags of blue marbles, with 10 marbles in each bag
    total_marbles = green_marbles + blue_marbles  # Calculate the total number of marbles Janelle has

    # Create a gift of 6 green marbles and 8 blue marbles
    gift_green = 6
    gift_blue = 8

    # Subtract the gift marbles from Janelle's total marbles
    total_marbles -= (gift_green + gift_blue)

    result = total_marbles
    return result

print(solution())