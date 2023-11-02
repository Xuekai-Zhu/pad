def solution():
    full_price = 60
    num_rackets = 2

    # Calculate the cost of the first racket at full price
    first_racket_cost = full_price

    # Calculate the cost of the second racket with the 50% discount
    second_racket_cost = full_price / 2

    # Calculate the total cost of both rackets
    total_cost = (first_racket_cost + second_racket_cost) * num_rackets
    result = total_cost
    return result

print(solution())