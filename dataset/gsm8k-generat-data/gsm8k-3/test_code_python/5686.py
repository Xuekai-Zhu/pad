def solution():
    """Linda owns a store. She sells jeans at 11 dollars each and tees at 8 dollars each. If she sold 7 tees and 4 jeans in a day, how much money, in dollars, did she have at the end of the day?"""
    
    # Define the price of jeans and tees
    JEANS_PRICE = 11
    TEES_PRICE = 8
    
    # Define the number of jeans and tees sold
    sold_jeans = 4
    sold_tees = 7
    
    # Calculate the total revenue from jeans and tees
    revenue_jeans = sold_jeans * JEANS_PRICE
    revenue_tees = sold_tees * TEES_PRICE
    
    # Calculate the total revenue
    total_revenue = revenue_jeans + revenue_tees
    
    # Display the total revenue
    result = total_revenue
    return result

print(solution())