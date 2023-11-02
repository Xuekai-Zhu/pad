def solution():
    total_people = 200
    male_adults = 60
    children = 80
    female_adults = total_people - male_adults - children
    result = female_adults
    return result

print(solution())