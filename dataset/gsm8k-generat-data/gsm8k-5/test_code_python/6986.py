def solution():
    distance = 200  # The event is 200 miles away from Briar's home
    cab_cost = 2.5  # A cab ride costs $2.5 per mile
    rides_per_day = 2  # Briar takes a cab ride to and from the event every day
    days = 7  # The event lasts for one week, or 7 days

    # Calculate the total cost of the cab rides for the entire event
    total_cost = distance * cab_cost * rides_per_day * days
    
    result = total_cost
    return result

print(solution())