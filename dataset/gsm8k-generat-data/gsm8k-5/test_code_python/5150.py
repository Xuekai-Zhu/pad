def solution():
    racket_price = 60  # The price of each racket
    discount_percent = 0.5  # The percentage of discount for the second racket
    num_rackets = 2  # Paul wants to buy 2 rackets

    # Calculate the total price Paul would have paid without any discounts
    total_price = racket_price * num_rackets

    # Calculate the price of the second racket after the discount
    discount_price = racket_price * discount_percent

    # Calculate the total price Paul actually paid with the discount
    actual_price = racket_price + discount_price

    # Calculate the total price Paul paid for both rackets
    total_actual_price = actual_price * num_rackets

    result = total_actual_price
    return result

print(solution())