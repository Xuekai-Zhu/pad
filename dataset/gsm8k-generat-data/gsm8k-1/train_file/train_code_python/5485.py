def solution():
    """Half of all the people in Nantucket will attend a planned meeting for a bowl game. There are 300 people in Nantucket, and the number of males going to the meeting is twice the number of females. How many females are going to the meeting?"""
    total_people = 300
    attendees = total_people / 2
    males = attendees * (2/3)
    females = attendees - males
    result = females
    return result

print(solution())