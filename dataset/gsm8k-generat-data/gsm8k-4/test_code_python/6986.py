def solution():
    """Briar is attending a one-week community empowerment event and has to take a cab ride to the event and back home every day. A cab ride costs $2.5 per mile. If the event is 200 miles away from Briar's home, calculate the total amount of money the cab rides cost would be at the end of the event?"""
    # Define the number of days Briar will be attending the event
    days = 7

    # Define the round trip distance to the event as 400 miles
    distance = 400

    # Define the cost per mile as $2.5
    cost_per_mile = 2.5

    # Calculate the total cost of cab rides
    total_cost = days * distance * cost_per_mile

    # return the result
    result = total_cost
    return result

print(solution())