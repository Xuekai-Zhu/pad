def solution():
    total_guests = 60
    male_guests = (total_guests / 3) * 2
    female_guests = total_guests - male_guests
    result = female_guests
    return result

print(solution())