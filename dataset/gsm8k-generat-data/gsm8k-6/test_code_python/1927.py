def solution():
    # Calculate the number of pamphlets Mike printed before and after his break
    mike_before_break = 600 * 9
    mike_after_break = (600/3) * 2
    
    # Calculate the number of hours Leo worked and his printing speed
    leo_hours = 9/3
    leo_speed = 600 * 2
    
    # Calculate the total number of pamphlets printed by both
    total_pamphlets = mike_before_break + mike_after_break + (leo_hours * leo_speed)
    result = total_pamphlets
    return result

print(solution())