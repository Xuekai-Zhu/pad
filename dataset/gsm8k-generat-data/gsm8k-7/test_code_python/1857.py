def solution():
    num_male_adults = 100
    num_female_adults = num_male_adults + 50
    total_adults = num_male_adults + num_female_adults
    num_children = total_adults * 2
    total_attendees = total_adults + num_children
    result = total_attendees
    return result

print(solution())