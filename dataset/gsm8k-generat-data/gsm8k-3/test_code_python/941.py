def solution():
    """Jean has 3 grandchildren.  She buys each grandkid 2 cards a year and puts $80 in each card.  How much does she give away to grandchildren a year?"""
    # Define the number of grandchildren and the amount put in each card
    NUM_GRANDKIDS = 3
    CARD_AMOUNT = 80

    # Calculate the total amount given away to grandchildren in a year
    total_amount = NUM_GRANDKIDS * 2 * CARD_AMOUNT

    # Display the total amount given away
    result = total_amount
    return result

print(solution())