def solution():
    
    mike_speed = 600
    mike_hours_1 = 9
    mike_hours_2 = 2
    leo_speed = 2 * mike_speed
    leo_hours = mike_hours_1 / 3
    
    mike_pamphlets_1 = mike_speed * mike_hours_1
    mike_pamphlets_2 = (mike_speed / 3) * mike_hours_2
    leo_pamphlets = leo_speed * leo_hours
    
    total_pamphlets = mike_pamphlets_1 + mike_pamphlets_2 + leo_pamphlets
    result = total_pamphlets
    return result

print(solution())