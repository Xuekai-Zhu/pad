def solution():
    """Half of all the people in Nantucket will attend a planned meeting for a bowl game. There are 300 people in Nantucket, and the number of males going to the meeting is twice the number of females. How many females are going to the meeting?"""
    # Define the total number of people in Nantucket and the number of people attending the meeting
    total_people = 300
    meeting_attendees = total_people / 2

    # Calculate the number of males attending the meeting
    male_attendees = meeting_attendees * (2/3)

    # Calculate the number of females attending the meeting
    female_attendees = meeting_attendees * (1/3)

    result = female_attendees
    return result

print(solution())