def solution():
    """Niles is collecting his book club's annual fees. Each of the six members pays $150/year towards snacks, plus $30 each for six hardcover books and $12 each for six paperback books. How much money does Niles collect in total?"""
    # Define the number of members and the costs of snacks, hardcover books, and paperback books
    NUM_MEMBERS = 6
    SNACKS_COST_PER_MEMBER = 150
    HARDCOVER_BOOK_COST_PER_MEMBER = 30
    PAPERBACK_BOOK_COST_PER_MEMBER = 12

    # Calculate the total cost of snacks for all members
    snacks_cost_total = NUM_MEMBERS * SNACKS_COST_PER_MEMBER

    # Calculate the total cost of hardcover books for all members
    hardcover_book_cost_total = NUM_MEMBERS * HARDCOVER_BOOK_COST_PER_MEMBER * 6

    # Calculate the total cost of paperback books for all members
    paperback_book_cost_total = NUM_MEMBERS * PAPERBACK_BOOK_COST_PER_MEMBER * 6

    # Calculate the total amount collected by Niles
    total_collected = snacks_cost_total + hardcover_book_cost_total + paperback_book_cost_total

    # Return the result
    result = total_collected
    return result

print(solution())