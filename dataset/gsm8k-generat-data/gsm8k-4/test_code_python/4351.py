def solution():
    """Joe’s mother gave him $56 to go to the store. Joe bought 7 notebooks and 2 books. Each notebook costs $4 and each book costs $7. How much money does Joe have left?"""
    # Define the amount of money Joe had
    money = 56

    # Calculate the cost of the notebooks
    notebook_cost = 7 * 4

    # Calculate the cost of the books
    book_cost = 2 * 7

    # Calculate the total cost of Joe's purchases
    total_cost = notebook_cost + book_cost

    # Calculate the amount of money Joe has left
    remaining_money = money - total_cost

    # return the result
    result = remaining_money
    return result

print(solution())