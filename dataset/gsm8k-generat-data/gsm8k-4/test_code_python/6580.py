def solution():
    """Toby is filling his swimming pool for the summer. The pool normally takes 50 hours to fill. He knows his hose runs at 100 gallons per hour. Water costs 1 cent for 10 gallons. How many dollars does it cost to fill the pool?"""
    # Define the time it takes to fill the pool and the flow rate of the hose
    hours = 50
    flow_rate = 100

    # Calculate the total amount of water needed to fill the pool
    total_water = flow_rate * hours

    # Calculate the total cost of the water
    cost_per_gallon = 0.1 # 1 cent per 10 gallons
    total_cost = total_water * cost_per_gallon

    # Convert the cost to dollars
    total_cost_in_dollars = total_cost / 100

    # Return the result
    result = total_cost_in_dollars
    return result

print(solution())