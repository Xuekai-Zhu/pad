def solution():
    """Heaven and her younger brother want to buy school supplies, so they ask their father for money, who gives them $100 in total to use. Heaven buys two sharpeners and four notebooks at $5 each, and her brother uses the remaining amount to buy ten erasers at $4 each and some highlighters. How much money did Heaven's brother spend on highlighters?"""
    # Define the price per item
    SHARPENER_PRICE = 5
    NOTEBOOK_PRICE = 5
    ERASER_PRICE = 4

    # Calculate the total amount spent by Heaven
    heaven_spent = 2 * SHARPENER_PRICE + 4 * NOTEBOOK_PRICE

    # Calculate the remaining amount after Heaven's purchase
    remaining_amount = 100 - heaven_spent

    # Calculate the amount spent by Heaven's brother on erasers
    eraser_spent = 10 * ERASER_PRICE

    # Calculate the amount remaining after purchasing erasers
    remaining_amount = remaining_amount - eraser_spent

    # Calculate the amount spent by Heaven's brother on highlighters
    highlighter_spent = remaining_amount

    # Return the result
    result = highlighter_spent
    return result

print(solution())