def solution():
    """Ping pong balls sell for $.10 each. Johnny buys 10000 for a prank. He gets a 30% discount for buying in such large bulk. How much does he pay?"""
    # Define the price of each ping pong ball and the bulk discount percentage
    PING_PONG_PRICE = 0.10
    BULK_DISCOUNT = 0.30

    # Define the number of ping pong balls purchased
    ping_pong_balls = 10000

    # Calculate the total cost before discount
    total_cost_before_discount = ping_pong_balls * PING_PONG_PRICE

    # Calculate the discount amount
    discount_amount = total_cost_before_discount * BULK_DISCOUNT

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost_before_discount - discount_amount

    # Display the total cost after discount
    result = total_cost_after_discount
    return result

print(solution())