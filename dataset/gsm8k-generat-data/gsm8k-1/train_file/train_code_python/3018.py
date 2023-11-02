def solution():
    """Janelle had 26 green marbles. Then she bought 6 bags of blue marbles. There were 10 marbles in each bag. She created a gift of 6 green marbles and 8 blue marbles and gave it to a friend. How many marbles does Janelle have now?"""
    green_marbles = 26
    blue_marbles = 6 * 10
    gift_green = 6
    gift_blue = 8
    total_marbles = green_marbles + blue_marbles - gift_green - gift_blue
    result = total_marbles
    return result

print(solution())