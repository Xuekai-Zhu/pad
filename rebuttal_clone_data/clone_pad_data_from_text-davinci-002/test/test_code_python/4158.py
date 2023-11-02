def solution():
    total_guests = 240
    percent_female = 60
    percent_jay_family = 50
    female_guests = total_guests * (percent_female / 100)
    female_jay_family = female_guests * (percent_jay_family / 100)
    result = female_jay_family
    return result

print(solution())