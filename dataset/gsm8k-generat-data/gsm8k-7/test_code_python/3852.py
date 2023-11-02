def solution():
    num_machines = 10
    ball_bearings_per_machine = 30
    regular_price_per_bb = 1.0
    sale_price_per_bb = 0.75
    bulk_discount = 0.2  # 20% discount

    # Calculate the total number of ball bearings needed
    total_bb_needed = num_machines * ball_bearings_per_machine

    # Calculate the regular cost of all ball bearings needed
    regular_cost = total_bb_needed * regular_price_per_bb

    # Calculate the sale price of all ball bearings needed
    sale_cost = total_bb_needed * sale_price_per_bb

    # Calculate the total cost after applying the bulk discount
    discounted_sale_cost = sale_cost * (1 - bulk_discount)

    # Calculate the amount saved by buying during the sale
    amount_saved = regular_cost - discounted_sale_cost
    result = amount_saved
    return result

print(solution())