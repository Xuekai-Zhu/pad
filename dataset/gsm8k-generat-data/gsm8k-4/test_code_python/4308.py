def solution():
    """John goes to the bakery to buy rolls. They sell them for 5 dollars for a dozen. He spent 15 dollars. How many rolls did he get?"""
    # Define the price per dozen and the total amount spent
    PRICE_PER_DOZEN = 5
    TOTAL_SPENT = 15

    # Calculate the number of dozens bought
    dozens_bought = TOTAL_SPENT / PRICE_PER_DOZEN

    # Calculate the number of rolls bought
    rolls_bought = dozens_bought * 12

    # return the result
    result = rolls_bought
    return result

print(solution())