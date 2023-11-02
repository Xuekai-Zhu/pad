def solution():
    needed_amount = 16  # in ounces

    # Option 1: buy one 16 oz package of store-brand butter
    option1_price = 7

    # Option 2: buy one 8 oz package and two 4 oz packages with a coupon
    option2_price = 4  # for the 8 oz package
    coupon_discount = 0.5  # 50% discount for each 4 oz package
    # calculate the price for two 4 oz packages after applying the coupon discount
    discounted_price = 2 * 2.0 * (1 - coupon_discount)
    option2_price += discounted_price  # add the price of the two 4 oz packages

    # Choose the lowest price option
    total_price = min(option1_price, option2_price)

    # Convert the price to cost per ounce
    cost_per_ounce = total_price / needed_amount
    result = cost_per_ounce
    return result

print(solution())