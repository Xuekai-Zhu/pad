def solution():
    """Mary and Jay are planning a wedding. Of the 240 guests, 60 percent are female. Of the females, 50 percent are from Jay's family. How many female guests are from Jay's family?"""
    total_guests = 240
    female_percentage = 0.6
    female_guests = total_guests * female_percentage
    jay_family_percentage = 0.5
    female_jay_family_guests = female_guests * jay_family_percentage
    result = female_jay_family_guests
    return result

print(solution())