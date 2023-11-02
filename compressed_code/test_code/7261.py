def solution():
    
    male_adults = 100
    female_adults = male_adults + 50
    total_adults = male_adults + female_adults
    children = 2 * total_adults
    total_attendees = male_adults + female_adults + children
    result = total_attendees
    return result

print(solution())