def solution():
    """John buys 500 newspapers. Each newspaper sells for $2. He sells 80% of them. He buys them all for 75% less than the price at which he sells them. How much profit does he make?"""
    # Define the number of newspapers and selling price per newspaper
    N_NEWSPAPERS = 500
    SELLING_PRICE = 2

    # Calculate the cost of buying all the newspapers at 75% discount
    BUYING_PRICE = SELLING_PRICE * 0.25

    # Calculate the cost of buying all the newspapers
    TOTAL_BUYING_COST = N_NEWSPAPERS * BUYING_PRICE

    #Calculate the number of newspapers sold and the total amount earned 
    N_SOLD_NEWSPAPERS = N_NEWSPAPERS * 0.8
    TOTAL_EARNED_AMOUNT = N_SOLD_NEWSPAPERS * SELLING_PRICE

    # Calculate the profit made 
    PROFIT = TOTAL_EARNED_AMOUNT - TOTAL_BUYING_COST

    result = PROFIT
    return result

print(solution())