def solution():
    total_people = 30 + 20
    people_left = 2/5 * total_people
    men_left = 9
    women_left = people_left - men_left
    women_remaining = 30 - women_left
    men_remaining = 20 - men_left
    difference = women_remaining - men_remaining
    result = difference
    return result

print(solution())