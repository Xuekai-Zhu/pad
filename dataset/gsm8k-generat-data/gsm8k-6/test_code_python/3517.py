def solution():
    # Calculate the cost per ounce of nuts before the coupon is applied
    cost_per_ounce = 25 / 40  # cost of a bag of nuts divided by the number of ounces in a bag

    # Calculate the cost per serving of nuts after the coupon is applied
    final_cost = cost_per_ounce - (5 / 40)  # subtract the $5 coupon from the cost and divide by the number of ounces in a bag
    cost_per_serving = final_cost * 100  # multiply by 100 to convert to cents

    result = cost_per_serving
    return result

print(solution())