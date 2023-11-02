def solution():
    
    total_items = 100
    lowella_percent = 35
    pamela_percent = lowella_percent * 1.2
    mandy_percent = pamela_percent * 2
    mandy_score = mandy_percent/100 * total_items
    result = mandy_score
    return result

print(solution())