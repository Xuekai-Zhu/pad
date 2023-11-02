def solution():
    
    total_people = 100
    women_percent = 50
    men_percent = 35
    children_percent = 100 - women_percent - men_percent
    children_count = (children_percent / 100) * total_people
    result = children_count
    return result

print(solution())