def solution():
    """John buys 5 toys that each cost $3. He gets a 20% discount. How much did he pay for everything?"""
    # Define the number of toys and the cost per toy
    num_toys = 5
    cost_per_toy = 3

    # Calculate the total cost before discount
    total_cost_before_discount = num_toys * cost_per_toy

    # Calculate the amount of the discount
    discount_percent = 20
    discount_amount = total_cost_before_discount * (discount_percent / 100)

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost_before_discount - discount_amount

    # Display the total cost after discount
    result = total_cost_after_discount
    return result

print(solution())