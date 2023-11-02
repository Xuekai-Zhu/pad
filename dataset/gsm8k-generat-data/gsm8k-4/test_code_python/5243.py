def solution():
    """With her savings, Sara bought two books: a book for 5.5£ and a book for 6.5£. She gives a 20£ bill to the seller. How much change does she get back?"""
    # Define the cost of the books and the amount of money given to the seller
    book1_cost = 5.5
    book2_cost = 6.5
    money_given = 20

    # Calculate the total cost of the books
    total_cost = book1_cost + book2_cost

    # Calculate the amount of change Sara gets back
    change = money_given - total_cost

    # return the result
    result = change
    return result

print(solution())