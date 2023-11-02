def solution():
    """Mark was caught speeding and the judge wants to make an example out of him. The base fine for speeding is $50 but additional penalties apply in this case.  The fine is increased by $2 for every mile per hour Mark was going over the speed limit. He was going 75 miles per hour in a 30 mile per hour zone. The fine is also doubled because he was in a school zone. Finally, the judge makes Mark pay $300 in court costs and he also has to pay his lawyer $80/hour for three hours of work. How much does Mark owe for this speeding ticket?"""
    # Define the base fine and the speed limit
    base_fine = 50
    speed_limit = 30

    # Calculate the fine for going over the speed limit
    over_limit = 75 - speed_limit
    fine_over_limit = over_limit * 2

    # Calculate the total fine
    total_fine = base_fine + fine_over_limit

    # Double the fine for being in a school zone
    total_fine *= 2

    # Add court costs and lawyer fees
    total_fine += 300 + (80 * 3)

    result = total_fine
    return result

print(solution())