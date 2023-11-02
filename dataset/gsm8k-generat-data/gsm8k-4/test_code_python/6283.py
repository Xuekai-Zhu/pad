def solution():
    """James decides to go to prom with Susan. He pays for everything. The tickets cost $100 each. Dinner is $120. He leaves a 30% tip. He also charters a limo for 6 hours that cost $80 per hour. How much did it all cost?"""
    # Define the cost of the prom tickets and dinner
    tickets_cost = 100 * 2
    dinner_cost = 120

    # Calculate the cost of the tip
    tip_cost = dinner_cost * 0.3

    # Calculate the cost of the limo
    limo_cost = 80 * 6

    # Calculate the total cost
    total_cost = tickets_cost + dinner_cost + tip_cost + limo_cost

    # Return the result
    result = total_cost
    return result

print(solution())