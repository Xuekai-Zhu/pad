def solution():
    peach_price = 0.4
    num_peaches = 400
    discount = 2
    purchase_threshold = 10

    # Calculate the total cost of all peaches
    total_peach_cost = num_peaches * peach_price

    # Calculate the number of $10 purchases made
    num_purchases = total_peach_cost // purchase_threshold

    # Calculate the total discount applied
    total_discount = num_purchases * discount

    # Calculate the total cost after discount
    total_cost = total_peach_cost - total_discount
    result = total_cost
    return result

print(solution())