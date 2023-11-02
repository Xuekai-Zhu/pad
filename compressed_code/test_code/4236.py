def solution():
    
    nantucket_people = 300
    attending_meeting = nantucket_people/2
    male_ratio = 2
    female_ratio = 1
    total_ratio = male_ratio + female_ratio
    female_attendees = (attending_meeting * female_ratio) / total_ratio
    result = female_attendees
    return result

print(solution())