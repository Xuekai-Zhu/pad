def solution():
    """Mark was caught speeding and the judge wants to make an example out of him. The base fine for speeding is $50 but additional penalties apply in this case.  The fine is increased by $2 for every mile per hour Mark was going over the speed limit. He was going 75 miles per hour in a 30 mile per hour zone. The fine is also doubled because he was in a school zone. Finally, the judge makes Mark pay $300 in court costs and he also has to pay his lawyer $80/hour for three hours of work. How much does Mark owe for this speeding ticket?"""

    # Calculate the base fine
    base_fine = 50

    # Calculate the additional fine
    over_limit = 75 - 30
    additional_fine = over_limit * 2

    # Double the fine due to school zone
    total_fine = (base_fine + additional_fine) * 2

    # Add court costs
    total_fine += 300

    # Add lawyer fees
    lawyer_fees = 80 * 3
    total_fine += lawyer_fees

    # Display the total amount Mark owes
    result = total_fine
    return result

print(solution())