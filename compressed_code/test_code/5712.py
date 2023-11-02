def solution():
    
    total_guests = 240
    female_percentage = 0.6
    female_guests = total_guests * female_percentage
    jay_family_percentage = 0.5
    female_jay_family_guests = female_guests * jay_family_percentage
    result = female_jay_family_guests
    return result

print(solution())