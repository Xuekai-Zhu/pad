def solution():
    """A new movie gets released and makes $120 million in the box office for its opening weekend. It ends up making 3.5 times that much during its entire run. If the production company gets to keep 60%, how much profit did they make if the movie cost $60 million to produce?"""
    # Define the opening weekend revenue and the multiplier for total revenue
    opening_weekend = 120
    total_multiplier = 3.5

    # Calculate the total revenue
    total_revenue = opening_weekend * total_multiplier

    # Calculate the production cost
    production_cost = 60

    # Calculate the profit
    profit = total_revenue * 0.6 - production_cost

    # return the result
    result = profit
    return result

print(solution())