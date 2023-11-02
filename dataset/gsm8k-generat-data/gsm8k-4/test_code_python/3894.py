def solution():
    """Tony drives a car that gets 25 miles to the gallon. He drives 50 miles round trip to work 5 days a week. His tank holds 10 gallons. He begins the week with a full tank and when he runs out he fills up at the local gas station for $2 a gallon. How much money does Tony spend on gas in 4 weeks?"""
    # Define the variables
    miles_per_gallon = 25
    miles_per_week = 50 * 5
    gallons_per_week = miles_per_week / miles_per_gallon
    tank_size = 10
    cost_per_gallon = 2
    weeks_in_month = 4

    # Calculate the total cost of gas for the month
    total_cost = 0
    for week in range(weeks_in_month):
        # Calculate the number of fill-ups needed for the week
        fillups_per_week = gallons_per_week / tank_size
        fillups_per_week = int(round(fillups_per_week, 0))
        
        # Calculate the total cost of gas for the week
        cost_per_week = fillups_per_week * tank_size * cost_per_gallon
        total_cost += cost_per_week

    result = total_cost
    return result

print(solution())