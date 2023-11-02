def solution():
    """Linda owns a store. She sells jeans at 11 dollars each and tees at 8 dollars each. If she sold 7 tees and 4 jeans in a day, how much money, in dollars, did she have at the end of the day?"""
    # Define the price of jeans and tees
    JEANS_PRICE = 11
    TEES_PRICE = 8

    # Define the number of jeans and tees sold
    jeans_sold = 4
    tees_sold = 7

    # Calculate the total amount of money earned
    total_money = (jeans_sold * JEANS_PRICE) + (tees_sold * TEES_PRICE)

    # return the result
    result = total_money
    return result

print(solution())