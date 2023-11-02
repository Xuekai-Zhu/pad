def solution():
    """Toby is filling his swimming pool for the summer. The pool normally takes 50 hours to fill. He knows his hose runs at 100 gallons per hour. Water costs 1 cent for 10 gallons. How many dollars does it cost to fill the pool?"""
    # Define the number of hours it takes to fill the pool and the hose's flow rate
    hours = 50
    hose_rate = 100 # gallons per hour

    # Calculate the number of gallons needed to fill the pool
    pool_volume = 50000 # gallons
    gallons_needed = pool_volume / hose_rate * hours

    # Calculate the cost to fill the pool
    cost_per_gallon = 0.001 # dollars
    cost = gallons_needed / 10 * cost_per_gallon

    # Display the cost to fill the pool
    result = cost
    return result

print(solution())