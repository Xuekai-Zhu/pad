def solution():
    """Sofia went to the department store to buy a pair of shoes and 2 shirts. A shirt costs $7 while a pair of shoes is $3 more than the shirt. If she decides to buy a bag which costs half the total price of the 2 shirts and a pair of shoes, how much will she pay for all those items?"""
    # Define the cost of a shirt and a pair of shoes
    SHIRT_COST = 7
    SHOE_COST = SHIRT_COST + 3

    # Calculate the total cost of two shirts and a pair of shoes
    total_cost = 2 * SHIRT_COST + 1 * SHOE_COST

    # Calculate the cost of the bag
    bag_cost = total_cost / 2

    # Calculate the total cost of all items
    total_cost += bag_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())