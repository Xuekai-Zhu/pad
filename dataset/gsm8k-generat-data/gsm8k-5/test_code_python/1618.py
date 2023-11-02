def solution():
    # Calculate the price of the cheaper pair of shoes
    cheaper_pair_price = 40 / 2  # Half of the original price of $40

    # Calculate the total price before the extra discount
    total_price_before_discount = cheaper_pair_price + 60  # Adding the price of the cheaper pair and the second pair

    # Calculate the amount of the extra discount
    extra_discount = total_price_before_discount / 4

    # Calculate the total amount after the extra discount
    total_price_after_discount = total_price_before_discount - extra_discount

    result = total_price_after_discount
    return result

print(solution())