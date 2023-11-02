def solution():
    """It will cost $60 to rent a sailboat and $80 per hour to rent a ski boat. Ken rented a sailboat while Aldrich rented a ski boat. How much more did it cost Aldrich to rent the ski boat than Ken to rent a sailboat for three hours a day in two days?"""
    # Define the rental costs
    sailboat_cost = 60
    skiboat_rental = 80

    # Calculate Ken's rental cost
    ken_rental = sailboat_cost * 2 * 3

    # Calculate Aldrich's rental cost
    aldrich_rental = skiboat_rental * 3 * 2

    # Calculate the difference between the two rental costs
    rental_cost_difference = aldrich_rental - ken_rental

    result = rental_cost_difference
    return result

print(solution())