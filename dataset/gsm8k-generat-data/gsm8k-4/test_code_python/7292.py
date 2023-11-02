def solution():
    """Marta was about to start the school year and needed to buy the necessary textbooks. She managed to buy five on sale, for $10 each. She had to order two textbooks online, which cost her a total of $40, and three she bought directly from the bookstore for a total of three times the cost of the online ordered books. How much in total did Martha spend on textbooks?"""
    # Define the cost of the textbooks bought on sale
    sale_textbooks_cost = 5 * 10

    # Define the cost of the textbooks ordered online
    online_textbooks_cost = 40

    # Define the cost of the textbooks bought directly from the bookstore
    bookstore_textbooks_cost = 3 * online_textbooks_cost

    # Calculate the total cost of all textbooks
    total_textbooks_cost = sale_textbooks_cost + online_textbooks_cost + bookstore_textbooks_cost

    # return the result
    result = total_textbooks_cost
    return result

print(solution())