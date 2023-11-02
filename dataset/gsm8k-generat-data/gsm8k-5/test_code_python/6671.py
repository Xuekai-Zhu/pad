def solution():
    total_attendees = 100  # 100 people attended the party
    women_percentage = 50  # 50% of the attendees are women
    men_percentage = 35  # 35% of the attendees are men

    # Calculate the number of women and men at the party
    women = total_attendees * (women_percentage / 100)
    men = total_attendees * (men_percentage / 100)

    # Calculate the number of children at the party
    children = total_attendees - women - men
    result = children
    return result

print(solution())