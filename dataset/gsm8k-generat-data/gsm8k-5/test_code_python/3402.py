def solution():
    ticket_price = 8
    popcorn_price = 5  # A bucket of popcorn costs $3 less than a movie ticket
    drink_price = popcorn_price + 1  # A drink costs $1 more than a bucket of popcorn
    candy_price = drink_price / 2  # A box of candy costs half as much as a drink

    # Calculate the total cost of buying a ticket, popcorn, drink, and candy separately
    total_normal_price = ticket_price + popcorn_price + drink_price + candy_price

    # Calculate the amount saved by getting the movie deal
    savings = total_normal_price - 20
    result = savings
    return result

print(solution())