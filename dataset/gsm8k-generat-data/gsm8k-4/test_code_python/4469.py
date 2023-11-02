def solution():
    """Ali's class wants to order 35 English textbooks and 35 geography textbooks. Knowing that a geography book costs $10.50 and that an English book costs $7.50, what is the amount of this order?"""
    # Define the number of English and geography textbooks
    english_books = 35
    geography_books = 35

    # Define the cost of an English and geography textbook
    english_cost = 7.5
    geography_cost = 10.5

    # Calculate the total cost of the order
    total_cost = (english_books * english_cost) + (geography_books * geography_cost)

    result = total_cost
    return result

print(solution())