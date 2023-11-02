def solution():
    goal = 90  # The cost of the clarinet is $90
    savings = 10  # Tara already has $10 saved
    book_price = 5  # Tara can sell her books for $5 each
    books_needed = (goal - savings) // book_price  # Calculate how many books Tara needs to sell to reach her goal

    # Sell books until halfway to the goal, then start over
    while savings < goal/2:
        savings += book_price
        books_needed -= 1

    # Continue selling books until goal is reached
    while savings < goal:
        savings += book_price
        books_needed += 1

    result = books_needed
    return result

print(solution())