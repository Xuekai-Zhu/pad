def solution():
    """Mary and Jay are planning a wedding. Of the 240 guests, 60 percent are female. Of the females, 50 percent are from Jay's family. How many female guests are from Jay's family?"""
    total_guests = 240
    female_percent = 60
    female_guests = total_guests * (female_percent / 100)
    jays_female_guests = female_guests * (50 / 100)
    result = jays_female_guests
    return result

print(solution())