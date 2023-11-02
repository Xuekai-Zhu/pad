def solution():
    '''Tom decides to open a theater. He knows it will cost $5 per square foot of space that he
    needs and he needs 12 square feet for every seat in his theater. He wants a 500 seat theater.
    He also realizes construction will cost twice as much as the land. He has a partner who covers
    40% of the cost. How much does Tom spend?'''
    seats = 500
    space_per_seat = 12
    space_needed = seats * space_per_seat
    land_cost = space_needed * 5
    construction_cost = land_cost * 2
    total_cost = land_cost + construction_cost
    tom_share = total_cost * 0.6  
    result = tom_share
    
    return result

print(solution())