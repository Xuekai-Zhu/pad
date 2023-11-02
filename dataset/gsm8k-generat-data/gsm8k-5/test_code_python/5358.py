def solution():
    peach_price = 0.4  # The price of one peach is 40 cents
    peaches_bought = 400  # Kataleya bought 400 peaches
    total_price = peach_price * peaches_bought  # The total price of the peaches without any discounts

    # Calculate the number of discounts Kataleya is eligible for
    num_discounts = total_price // 10

    # Calculate the total discount Kataleya is eligible for
    total_discount = num_discounts * 2

    # Calculate the final price Kataleya pays after all discounts
    final_price = total_price - total_discount
    result = final_price
    return result

print(solution())