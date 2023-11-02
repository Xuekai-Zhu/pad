def solution():
    """Niles is collecting his book club's annual fees. Each of the six members pays $150/year towards snacks, plus $30 each for six hardcover books and $12 each for six paperback books. How much money does Niles collect in total?"""
    # Define the cost for snacks, hardcover books, and paperback books
    SNACK_COST = 150
    HARDCOVER_COST = 30
    PAPERBACK_COST = 12

    # Define the number of members in the book club
    NUM_MEMBERS = 6

    # Calculate the total cost for snacks
    snack_total = NUM_MEMBERS * SNACK_COST

    # Calculate the total cost for hardcover books
    hardcover_total = NUM_MEMBERS * HARDCOVER_COST * 6

    # Calculate the total cost for paperback books
    paperback_total = NUM_MEMBERS * PAPERBACK_COST * 6

    # Calculate the total money collected
    total_collected = snack_total + hardcover_total + paperback_total

    # Display the total money collected
    result = total_collected
    return result

print(solution())