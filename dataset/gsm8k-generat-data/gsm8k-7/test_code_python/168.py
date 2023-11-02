def solution():
    quiche_price = 15
    num_quiches = 2

    croissant_price = 3
    num_croissants = 6

    biscuit_price = 2
    num_biscuits = 6

    advanced_order_discount = 0.1

    # Calculate the total cost of all items before the discount
    total_cost_before_discount = (quiche_price * num_quiches) + (croissant_price * num_croissants) + (
                biscuit_price * num_biscuits)

    # Check if the total cost is over $50.00
    if total_cost_before_discount > 50:
        # Calculate the discounted amount
        discount_amount = total_cost_before_discount * advanced_order_discount

        # Calculate the total cost after the discount
        total_cost_after_discount = total_cost_before_discount - discount_amount
    else:
        # If the total cost is not over $50.00, there is no discount
        total_cost_after_discount = total_cost_before_discount

    result = total_cost_after_discount
    return result

print(solution())