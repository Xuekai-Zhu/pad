def solution():
    
    total_chairs = 40
    capacity_per_chair = 2
    unoccupied_chairs = total_chairs * (2/5)
    occupied_chairs = total_chairs - unoccupied_chairs
    total_attendees = occupied_chairs * capacity_per_chair
    result = total_attendees
    
    return result

print(solution())