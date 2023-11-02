def solution():
    # Calculate the total number of trash cans originally in Central Park
    central_park_cans = (24 * 2) - 8  # 8 more than half of the number of trash cans in Veteran's Park
    
    # Calculate the number of trash cans moved from Central Park to Veteran's Park
    moved_cans = central_park_cans / 2  # half of the trash cans in Central Park
    
    # Calculate the number of trash cans in Veteran's Park after the move
    new_veterans_cans = 24 + moved_cans
    
    result = new_veterans_cans
    return result

print(solution())