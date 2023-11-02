def solution():
    """Joe’s mother gave him $56 to go to the store. Joe bought 7 notebooks and 2 books. Each notebook costs $4 and each book costs $7. How much money does Joe have left?"""
    # Define the cost of each item
    NOTEBOOK_PRICE = 4
    BOOK_PRICE = 7

    # Define the number of each item purchased
    notebook_count = 7
    book_count = 2

    # Calculate the total cost of the notebooks
    notebook_cost = notebook_count * NOTEBOOK_PRICE

    # Calculate the total cost of the books
    book_cost = book_count * BOOK_PRICE

    # Calculate the total cost of all the items
    total_cost = notebook_cost + book_cost

    # Calculate how much money Joe has left
    money_left = 56 - total_cost

    # Display how much money Joe has left
    result = money_left
    return result

print(solution())