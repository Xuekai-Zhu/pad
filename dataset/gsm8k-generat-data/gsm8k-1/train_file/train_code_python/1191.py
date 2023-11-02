def solution():
    """Out of the 120 people who attended the party, 1/3 are men while half are women. The rest are children. How many children attended the party?"""
    total_attendees = 120
    men = total_attendees / 3
    women = total_attendees / 2
    children = total_attendees - men - women
    result = children
    return result

print(solution())