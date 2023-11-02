def solution():
    """Princeton had a gender reveal party and invited all of his fellow employees to celebrate with him. If the total number of guests were 60, and 2/3 were male guests, how many female guests attended the party?"""
    total_guests = 60
    male_guests = total_guests * (2/3)
    female_guests = total_guests - male_guests
    result = female_guests
    return result

print(solution())