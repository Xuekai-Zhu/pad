def solution():
    necklace_price = 34  # The necklace costs $34
    book_price = necklace_price + 5  # The book is $5 more expensive than the necklace
    total_cost = necklace_price + book_price  # Calculate the total cost of the necklace and book

    limit = 70  # Bob set a limit of $70

    # Calculate how much Bob went over his limit
    over_limit = total_cost - limit
    result = over_limit
    return result

print(solution())