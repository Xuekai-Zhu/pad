def solution():
    """Heaven and her younger brother want to buy school supplies, so they ask their father for money, who gives them $100 in total to use. Heaven buys two sharpeners and four notebooks at $5 each, and her brother uses the remaining amount to buy ten erasers at $4 each and some highlighters. How much money did Heaven's brother spend on highlighters?"""
    # Calculate the total cost of Heaven's purchases
    heaven_cost = 2 * 5 + 4 * 5

    # Calculate the remaining amount of money for Heaven's brother
    remaining_money = 100 - heaven_cost

    # Calculate the cost of the erasers
    eraser_cost = 10 * 4

    # Calculate the cost of the highlighters
    highlighter_cost = remaining_money - eraser_cost

    # Display the cost of the highlighters
    result = highlighter_cost
    return result

print(solution())