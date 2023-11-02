def solution():
    """Ali's class wants to order 35 English textbooks and 35 geography textbooks. Knowing that a geography book costs $10.50 and that an English book costs $7.50, what is the amount of this order?"""
    # Define the cost of each type of textbook
    ENGLISH_PRICE = 7.5
    GEOGRAPHY_PRICE = 10.5

    # Define the number of each type of textbook ordered
    english_books = 35
    geography_books = 35

    # Calculate the total cost of the English textbooks
    english_cost = english_books * ENGLISH_PRICE

    # Calculate the total cost of the geography textbooks
    geography_cost = geography_books * GEOGRAPHY_PRICE

    # Calculate the total cost of the order
    total_cost = english_cost + geography_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())