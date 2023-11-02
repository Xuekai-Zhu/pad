def solution():
    
    mike_hours_1 = 9
    mike_speed_1 = 600
    mike_pamphlets_1 = mike_hours_1 * mike_speed_1
    
    mike_hours_2 = 2
    mike_speed_2 = mike_speed_1 / 3
    mike_pamphlets_2 = mike_hours_2 * mike_speed_2
    
    leo_hours = mike_hours_1 / 3
    leo_speed = 2 * mike_speed_1
    leo_pamphlets = leo_hours * leo_speed
    
    total_pamphlets = mike_pamphlets_1 + mike_pamphlets_2 + leo_pamphlets
    result = total_pamphlets
    return result

print(solution())