def solution():
    """An elevator is on the 9th floor. It goes down 7 floors, then up 3 floors, then up 8 floors. If the elevator is on the top floor, how many floors are there in the building?"""
    current_floor = 9
    current_floor -= 7 # moves down 7 floors
    current_floor += 3 # moves up 3 floors
    current_floor += 8 # moves up 8 floors
    
    # the elevator is on the top floor, so the building has current_floor floors
    result = current_floor
    return result

print(solution())