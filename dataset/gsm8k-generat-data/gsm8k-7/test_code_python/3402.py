def solution():
    deal_price = 20

    ticket_price = 8
    popcorn_price = 5
    drink_price = popcorn_price + 1
    candy_price = drink_price / 2

    # Calculate the normal price of a ticket, popcorn, drink, and candy
    normal_price = ticket_price + popcorn_price + drink_price + candy_price

    # Calculate the savings from the deal
    savings = normal_price - deal_price
    result = savings
    return result

print(solution())