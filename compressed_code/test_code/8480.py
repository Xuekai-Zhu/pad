def solution():
    
    couples_rooms = 13
    single_rooms = 14
    total_customers = (couples_rooms * 2) + single_rooms
    ml_per_bath = 10
    total_ml = total_customers * ml_per_bath
    result = total_ml
    return result

print(solution())