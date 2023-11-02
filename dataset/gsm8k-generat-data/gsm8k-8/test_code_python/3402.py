def solution():
    # Define the normal prices
    ticket_price = 8
    popcorn_price = ticket_price - 3
    drink_price = popcorn_price + 1
    candy_price = drink_price / 2

    # Calculate the total normal cost
    total_normal_cost = ticket_price + popcorn_price + drink_price + candy_price

    # Calculate the savings from the deal
    savings = total_normal_cost - 20
    result = savings
    return result

print(solution())