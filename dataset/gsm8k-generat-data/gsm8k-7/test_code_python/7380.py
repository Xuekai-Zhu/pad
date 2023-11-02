def solution():
    total_guests = 240
    female_percentage = 0.6
    jay_female_percentage = 0.5

    # Calculate the total number of female guests
    female_guests = total_guests * female_percentage

    # Calculate the number of female guests from Jay's family
    jay_female_guests = female_guests * jay_female_percentage
    result = jay_female_guests
    return result

print(solution())