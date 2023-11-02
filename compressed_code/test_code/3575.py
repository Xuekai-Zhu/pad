def solution():
    
    former_speed = 40
    former_hours = 600 / former_speed
    new_speed = former_speed * 1.5
    new_hours = former_hours - 4
    new_pages = new_speed * new_hours
    result = new_pages
    return result

print(solution())