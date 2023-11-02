def solution():
    """Briar is attending a one-week community empowerment event and has to take a cab ride to the event and back home every day. A cab ride costs $2.5 per mile. If the event is 200 miles away from Briar's home, calculate the total amount of money the cab rides cost would be at the end of the event?"""
    # Define the cost per mile of a cab ride
    COST_PER_MILE = 2.5

    # Define the distance to the event
    distance = 200

    # Calculate the total cost of the cab rides for the week
    total_cost = distance * 2 * 7 * COST_PER_MILE

    # Display the total cost
    result = total_cost
    return result

print(solution())