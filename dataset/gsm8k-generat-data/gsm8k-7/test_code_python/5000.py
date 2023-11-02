def solution():
    hamburger_meat = 5.0
    crackers = 3.5
    num_veggie_bags = 4
    veggie_price = 2.0
    cheese = 3.5
    discount = 0.1 # 10% discount for being a store rewards member

    # Calculate the total cost of all items before discount
    total_cost = hamburger_meat + crackers + (num_veggie_bags * veggie_price) + cheese

    # Calculate the discount amount
    discount_amount = total_cost * discount

    # Calculate the total cost after discount
    total_cost -= discount_amount

    result = total_cost
    return result

print(solution())