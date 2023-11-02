def solution():
    """Jack bought 3 books a month at $20 each. He sells them back at the end of the year for $500. How much money did he lose?"""
    # Define the cost of one book
    book_cost = 20

    # Calculate the total cost of buying 3 books per month
    total_cost = book_cost * 3 * 12

    # Calculate the loss from selling the books back
    loss = total_cost - 500

    # return the result
    result = loss
    return result

print(solution())