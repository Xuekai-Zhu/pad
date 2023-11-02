def solution():
    # Calculate the total number of people attending the meeting
    total_people = 0.5 * 300

    # Calculate the number of males attending the meeting
    male_count = total_people / 3

    # Calculate the number of females attending the meeting
    female_count = total_people - male_count

    result = female_count
    return result

print(solution())