def solution():
    regular_price = 40.00  # Regular price for a mani/pedi is $40.00
    discount = 0.25  # The salon is offering a 25% discount for Mother's Day
    num_services = 5  # Charlotte is getting mani/pedis for herself, her daughter, and 3 granddaughters

    # Calculate the total cost before discount
    total_cost_before_discount = regular_price * num_services

    # Calculate the discount amount
    discount_amount = total_cost_before_discount * discount

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost_before_discount - discount_amount

    result = total_cost_after_discount
    return result

print(solution())