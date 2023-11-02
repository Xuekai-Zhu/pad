def solution():
    """Shelby had $20 to take to the book fair. She bought one book for $8 and another for $4. She decided to buy as many $4 posters as she could with the money she had left. How many posters can she buy?"""
    # Define the prices of the books and posters
    book1_price = 8
    book2_price = 4
    poster_price = 4

    # Calculate the total amount spent on books
    total_books_cost = book1_price + book2_price

    # Calculate the amount of money still available for posters
    money_left_for_posters = 20 - total_books_cost

    # Calculate the number of posters Shelby can buy
    posters_bought = money_left_for_posters // poster_price

    # Display the number of posters Shelby can buy
    result = posters_bought
    return result

print(solution())