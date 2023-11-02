def solution():
    
    original_speed = 40
    original_hours = 600 / original_speed
    new_speed = original_speed * 1.5
    new_hours = original_hours - 4
    new_pages = new_speed * new_hours
    result = new_pages
    return result

print(solution())