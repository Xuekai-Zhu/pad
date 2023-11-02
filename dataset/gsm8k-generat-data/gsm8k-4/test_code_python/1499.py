def solution():
    """A taco truck is selling soft tacos for $2 and hard shell tacos for $5 during the lunch rush. The first group of customers is a family that buys four hard shell tacos and three soft tacos. The rest of the customers in the lunch rush only buy two soft tacos each. There were ten customers after the family. How many dollars did the taco truck make during the lunch rush?"""
    # Define the prices of soft and hard shell tacos
    soft_price = 2
    hard_price = 5

    # Calculate the total cost of the family's order
    family_cost = (4 * hard_price) + (3 * soft_price)

    # Calculate the total cost of the remaining customers' orders
    remaining_customers = 10
    remaining_cost = remaining_customers * (2 * soft_price)

    # Calculate the total revenue of the taco truck during the lunch rush
    total_revenue = family_cost + remaining_cost

    # return the result
    result = total_revenue
    return result

print(solution())