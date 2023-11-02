def solution():
    first_shoes_price = 40
    second_shoes_price = 60
    discount_rate = 0.5
    extra_discount_rate = 0.25

    # Calculate the discounted price of the second pair of shoes
    discounted_second_price = second_shoes_price * discount_rate

    # Determine which pair of shoes is cheaper after the discount is applied
    if discounted_second_price < first_shoes_price:
        cheaper_price = discounted_second_price
        expensive_price = first_shoes_price
    else:
        cheaper_price = first_shoes_price
        expensive_price = discounted_second_price

    # Calculate the total cost of both pairs of shoes before applying the extra discount
    total_cost = cheaper_price + expensive_price

    # Calculate the final cost after applying the extra discount
    final_cost = total_cost * (1 - extra_discount_rate)

    result = final_cost
    return result

print(solution())