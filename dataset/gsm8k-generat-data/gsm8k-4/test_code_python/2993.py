def solution():
    """A store gives a 10% discount for the amount of the sell that was over $1000. John buys 7 items that each cost $200. What does his order cost after the discount?"""
    # Define the cost of each item and the number of items purchased
    item_cost = 200
    num_items = 7

    # Calculate the total cost of the purchase
    total_cost = item_cost * num_items

    # Calculate the discount on the amount over $1000
    discount = 0
    if total_cost > 1000:
        discount = 0.1 * (total_cost - 1000)

    # Calculate the final cost after the discount
    final_cost = total_cost - discount

    result = final_cost
    return result

print(solution())