def solution():
    """Marta was about to start the school year and needed to buy the necessary textbooks. She managed to buy five on sale, for $10 each. She had to order two textbooks online, which cost her a total of $40, and three she bought directly from the bookstore for a total of three times the cost of the online ordered books. How much in total did Martha spend on textbooks?"""
    # Define the cost of each discounted textbook
    DISCOUNTED_PRICE = 10

    # Calculate the total cost of the discounted textbooks
    discounted_cost = 5 * DISCOUNTED_PRICE

    # Calculate the cost of the online ordered textbooks
    online_cost = 40

    # Calculate the cost of the bookstore textbooks
    bookstore_cost = 3 * online_cost

    # Calculate the total cost of all the textbooks
    total_cost = discounted_cost + online_cost + bookstore_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())