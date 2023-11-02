def solution():
    
    total_people = 5000
    voted_by_midday = total_people * (2/5)
    remaining_people = total_people - voted_by_midday
    voted_by_16 = remaining_people * (2/3)
    not_voted_by_16 = remaining_people - voted_by_16
    result = not_voted_by_16
    return result

print(solution())