def solution():
    """It will cost $60 to rent a sailboat and $80 per hour to rent a ski boat. Ken rented a sailboat while Aldrich rented a ski boat. How much more did it cost Aldrich to rent the ski boat than Ken to rent a sailboat for three hours a day in two days?"""
    # Define the cost to rent a sailboat and ski boat
    SAILBOAT_COST = 60
    SKI_BOAT_COST_PER_HOUR = 80

    # Calculate the total cost for Ken's sailboat rental
    ken_total_cost = SAILBOAT_COST * 2 * 3

    # Calculate the total cost for Aldrich's ski boat rental
    aldrich_total_cost = (SKI_BOAT_COST_PER_HOUR * 3 * 2) + 60

    # Calculate the difference in cost between the two rentals
    cost_difference = aldrich_total_cost - ken_total_cost

    # Display the cost difference
    result = cost_difference
    return result

print(solution())