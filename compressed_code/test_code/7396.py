def solution():
    
    women_haircut_time = 50
    men_haircut_time = 15
    kids_haircut_time = 25
    num_women = 3
    num_men = 2
    num_kids = 3
    total_time = (women_haircut_time * num_women) + (men_haircut_time * num_men) + (kids_haircut_time * num_kids)
    result = total_time
    return result

print(solution())