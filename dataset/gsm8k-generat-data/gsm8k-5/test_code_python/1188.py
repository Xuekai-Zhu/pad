def solution():
    sandwich_price = 5  # Preston charges $5 per sandwich
    delivery_fee = 20  # Preston charges $20 for delivery
    num_sandwiches = 18  # Abra Company orders 18 sandwiches
    tip_percent = 0.1  # Abra Company tips 10% of the total order

    # Calculate the total cost of the sandwiches
    total_sandwich_cost = sandwich_price * num_sandwiches

    # Calculate the total order amount, including the delivery fee
    total_order_amount = total_sandwich_cost + delivery_fee

    # Calculate the tip amount
    tip_amount = total_order_amount * tip_percent

    # Calculate the total amount Preston received
    total_amount = total_order_amount + tip_amount
    result = total_amount
    return result

print(solution())