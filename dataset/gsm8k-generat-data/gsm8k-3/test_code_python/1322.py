def solution():
    """Tom decides to open a theater.  He knows it will cost $5 per square foot of space that he needs and he needs 12 square feet for every seat in his theater.  He wants a 500 seat theater.  He also realizes construction will cost twice as much as the land.  He has a partner who covers 40% of the cost.  How much does Tom spend?"""
    # Define the cost per square foot of space
    SPACE_COST = 5

    # Define the space needed per seat
    SPACE_PER_SEAT = 12

    # Define the number of seats needed
    SEAT_COUNT = 500

    # Calculate the total space needed
    space_needed = SPACE_PER_SEAT * SEAT_COUNT

    # Calculate the cost of the land
    land_cost = space_needed * SPACE_COST

    # Calculate the cost of construction
    construction_cost = land_cost * 2

    # Calculate the total cost
    total_cost = land_cost + construction_cost

    # Calculate the cost covered by Tom's partner
    partner_contribution = total_cost * 0.4

    # Calculate the amount Tom spends
    tom_spends = total_cost - partner_contribution

    result = tom_spends
    return result

print(solution())