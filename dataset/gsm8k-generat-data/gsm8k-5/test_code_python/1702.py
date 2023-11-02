def solution():
    total_guests = 60  # Total number of guests at the party
    male_guests = (2/3) * total_guests  # Number of male guests
    female_guests = total_guests - male_guests  # Number of female guests

    result = female_guests
    return result

print(solution())