def solution():
    # Define the cost of the clarinet
    clarinet_cost = 90

    # Define the amount Tara has already saved
    saved_amount = 10

    # Define the cost of one book
    book_cost = 5

    # Calculate the total number of books Tara needs to sell
    total_books = (clarinet_cost - saved_amount) / book_cost

    # Calculate the halfway mark
    halfway = (clarinet_cost + saved_amount) / 2

    # If Tara loses her savings, she needs to sell twice as many books
    if halfway > saved_amount + total_books * book_cost:
        total_books *= 2

    result = total_books
    return result

print(solution())