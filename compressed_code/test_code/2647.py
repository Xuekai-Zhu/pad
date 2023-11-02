def solution():
    
    couples_rooms = 13
    single_rooms = 14
    total_rooms = couples_rooms + single_rooms
    ml_per_bath = 10
    total_baths = couples_rooms * 2 + single_rooms
    total_ml_needed = total_baths * ml_per_bath
    result = total_ml_needed
    return result

print(solution())