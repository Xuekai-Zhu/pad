def solution():
    num_men = 4
    num_women_in_meeting = 6
    decrease_in_women = 0.2

    # Calculate the total number of women in the office before the meeting
    total_women_before = num_women_in_meeting / (1 - decrease_in_women)

    # Calculate the total number of men and women in the office before the meeting
    total_people_before = 2 * total_women_before

    # Calculate the total number of people in the office after the meeting
    total_people_after = total_people_before - num_men - num_women_in_meeting

    result = total_people_after
    return result

print(solution())