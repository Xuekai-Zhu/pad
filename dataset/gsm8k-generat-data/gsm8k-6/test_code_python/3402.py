def solution():
    # Calculate the total cost of a movie ticket, popcorn, drink, and candy if bought separately
    ticket_cost = 8
    popcorn_cost = 5
    drink_cost = popcorn_cost + 1
    candy_cost = drink_cost / 2
    normal_cost = ticket_cost + popcorn_cost + drink_cost + candy_cost

    # Calculate the amount saved by buying the combo deal
    combo_price = 20
    saved_amount = normal_cost - combo_price
    result = round(saved_amount, 2)
    return result

print(solution())