def solution():
    """Chalktown High School had their prom last weekend. There were 123 students who attended. If 3 students attended on their own, how many couples came to the prom?"""
    total_attendees = 123
    solo_attendees = 3
    couple_attendees = (total_attendees - solo_attendees) / 2
    result = couple_attendees
    return result

print(solution())