def solution():
    num_nieces = 3  # Eve has 3 nieces to buy cooking gear for
    cost_mitts = 14.00
    cost_apron = 16.00
    cost_utensils = 10.00
    cost_knife = 2 * cost_utensils  # The small knife costs twice the amount of the utensils

    # Calculate the total cost of the cooking gear before the sale
    total_cost_before_sale = (cost_mitts + cost_apron + cost_utensils + cost_knife) * num_nieces

    # Calculate the discount offered during the sale
    discount_percent = 0.25
    discount_amount = total_cost_before_sale * discount_percent

    # Calculate the total cost of the cooking gear after the sale
    total_cost_after_sale = total_cost_before_sale - discount_amount
    result = total_cost_after_sale
    return result

print(solution())