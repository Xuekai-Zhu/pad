def solution():
    male_adults = 100
    female_adults = male_adults + 50
    total_adults = male_adults + female_adults
    children = total_adults * 2
    total_people = total_adults + children
    result = total_people
    return result

print(solution())