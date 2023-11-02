def solution():
    # Calculate the total cost for Ken to rent a sailboat
    ken_sailboat_cost = 60 + (3 * 80)  # rent sailboat for 3 hours/day for 2 days

    # Calculate the total cost for Aldrich to rent a ski boat
    aldrich_skiboat_cost = (80 * 3 * 2)  # rent ski boat for 3 hours/day for 2 days

    # Calculate the difference in cost between renting a sailboat and ski boat
    cost_difference = aldrich_skiboat_cost - ken_sailboat_cost
    result = cost_difference
    return result

print(solution())