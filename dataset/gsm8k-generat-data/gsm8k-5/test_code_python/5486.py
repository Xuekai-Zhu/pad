def solution():
    total_people = 300  # There are 300 people in Nantucket
    attending_meeting = total_people / 2  # Half of the people in Nantucket will attend the meeting
    males_attending = attending_meeting * 2 / 3  # The number of males going to the meeting is 2/3 of the total number of attendees
    females_attending = attending_meeting * 1 / 3  # The number of females going to the meeting is 1/3 of the total number of attendees
    result = females_attending
    return result

print(solution())