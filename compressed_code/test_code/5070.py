def solution():
    
    initial_guests = 3 * 12
    additional_guests = initial_guests * (1/3)
    total_guests = initial_guests + additional_guests - 5
    total_chairs = total_guests + 12
    result = total_chairs
    return result

print(solution())