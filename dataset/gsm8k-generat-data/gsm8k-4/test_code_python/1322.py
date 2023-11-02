def solution():
    """Tom decides to open a theater. He knows it will cost $5 per square foot of space that he needs and he needs 12 square feet for every seat in his theater. He wants a 500 seat theater. He also realizes construction will cost twice as much as the land. He has a partner who covers 40% of the cost. How much does Tom spend?"""
    # Define the cost per square foot of space
    SPACE_COST_PER_SQ_FT = 5

    # Define the square footage required per seat
    SQ_FT_REQUIRED_PER_SEAT = 12

    # Define the number of seats in the theater
    NUM_SEATS = 500

    # Calculate the total square footage required for the theater
    total_sq_ft = NUM_SEATS * SQ_FT_REQUIRED_PER_SEAT

    # Calculate the cost of the land
    land_cost = total_sq_ft * SPACE_COST_PER_SQ_FT

    # Calculate the cost of construction
    construction_cost = land_cost * 2

    # Calculate the total cost
    total_cost = land_cost + construction_cost

    # Calculate Tom's portion of the cost
    tom_cost = total_cost * 0.6

    result = round(tom_cost)
    return result

print(solution())