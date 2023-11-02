def solution():
    """Tom decides to open a theater. He knows it will cost $5 per square foot of space that he needs and he needs 12 square feet for every seat in his theater. He wants a 500 seat theater. He also realizes construction will cost twice as much as the land. He has a partner who covers 40% of the cost. How much does Tom spend?"""
    seat_space = 12
    num_seats = 500
    total_space = seat_space * num_seats
    land_cost = total_space * 5
    construction_cost = land_cost * 2
    total_cost = land_cost + construction_cost
    partner_cover = 0.4
    tom_share = total_cost * (1 - partner_cover)
    result = tom_share
    return result

print(solution())