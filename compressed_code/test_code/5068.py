def solution():
    
    women_in_favor = 0.35
    women_opposed = 39
    total_women = women_opposed / (1 - women_in_favor)
    total_people = 2 * total_women
    result = total_people
    return result

print(solution())