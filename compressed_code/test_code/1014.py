def solution():
    
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