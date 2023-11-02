def solution():
    initial_amount = 20
    milk_price = 4.0
    bread_price = 3.5
    detergent_price = 10.25
    detergent_coupon = 1.25
    bananas_price_per_pound = 0.75
    bananas_weight = 2 # in pounds

    # Calculate the total cost of all items before any discounts or coupons
    total_cost_without_discounts = milk_price + bread_price + detergent_price - detergent_coupon + (bananas_price_per_pound * bananas_weight)

    # Calculate the discount for the milk
    milk_discount = milk_price / 2
    total_cost_with_discounts = total_cost_without_discounts - milk_discount

    # Calculate the amount spent and amount left over
    amount_spent = total_cost_with_discounts
    amount_left_over = initial_amount - amount_spent
    result = amount_left_over

    return result

print(solution())