def solution():
    
    total_people = 650
    adult_percentage = 0.8
    adult_count = total_people * adult_percentage
    child_count = total_people - adult_count
    result = child_count
    return result

print(solution())