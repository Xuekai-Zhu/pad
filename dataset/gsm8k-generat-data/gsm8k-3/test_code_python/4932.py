def solution():
    """A movie theater charges $5 for matinee tickets, $7 for evening tickets, and $10 for opening night tickets. A bucket of popcorn costs $10. On Friday, they had 32 matinee customers, 40 evening customers, and 58 customers for an opening night showing of a movie. If half the customers bought popcorn, how much money in dollars did the theater make on Friday night?"""
    # Define ticket prices and popcorn cost
    MATINEE_PRICE = 5
    EVENING_PRICE = 7
    OPENING_PRICE = 10
    POPCORN_PRICE = 10

    # Define number of customers
    matinee_customers = 32
    evening_customers = 40
    opening_customers = 58

    # Calculate ticket sales
    matinee_sales = MATINEE_PRICE * matinee_customers
    evening_sales = EVENING_PRICE * evening_customers
    opening_sales = OPENING_PRICE * opening_customers

    # Calculate popcorn sales
    popcorn_customers = (matinee_customers + evening_customers + opening_customers) / 2
    popcorn_sales = POPCORN_PRICE * popcorn_customers

    # Calculate total sales
    total_sales = matinee_sales + evening_sales + opening_sales + popcorn_sales

    # Display total sales
    result = total_sales
    return result

print(solution())