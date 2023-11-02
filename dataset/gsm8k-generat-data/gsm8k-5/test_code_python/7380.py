def solution():
    total_guests = 240  # the total number of guests
    female_percentage = 60  # the percentage of female guests
    females = total_guests * (female_percentage / 100)  # the total number of female guests
    jays_family_percentage = 50  # the percentage of female guests from Jay's family
    jays_family_females = females * (jays_family_percentage / 100)  # the total number of females from Jay's family
    result = jays_family_females
    return result

print(solution())