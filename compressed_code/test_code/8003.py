def solution():
    
    current_bedroom_sqft = 309
    current_bath_sqft = 150
    new_room_factor = 2
    new_room_sqft = (current_bedroom_sqft + current_bath_sqft) * new_room_factor
    result = new_room_sqft
    return result

print(solution())