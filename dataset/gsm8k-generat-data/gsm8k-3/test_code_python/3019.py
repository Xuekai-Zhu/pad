def solution():
    """Janelle had 26 green marbles. Then she bought 6 bags of blue marbles. There were 10 marbles in each bag.  She created a gift of 6 green marbles and 8 blue marbles and gave it to a friend. How many marbles does Janelle have now?"""
    # Define the number of green marbles Janelle started with
    green_marbles = 26

    # Define the number of blue marbles Janelle bought
    blue_marbles = 6 * 10

    # Define the number of green and blue marbles in the gift
    gift_green_marbles = 6
    gift_blue_marbles = 8

    # Calculate the total number of marbles Janelle has now
    total_marbles = green_marbles + blue_marbles - gift_green_marbles - gift_blue_marbles

    # Display the total number of marbles Janelle has now
    result = total_marbles
    return result

print(solution())