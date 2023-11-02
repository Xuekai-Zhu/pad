def solution():
    
    total_rabbits = 16
    monday_toys = 6
    wednesday_toys = monday_toys * 2
    friday_toys = monday_toys * 4
    saturday_toys = wednesday_toys / 2
    total_toys = monday_toys + wednesday_toys + friday_toys + saturday_toys
    toys_per_rabbit = total_toys / total_rabbits
    result = toys_per_rabbit
    return result

print(solution())