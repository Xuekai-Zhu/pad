def solution():
    
    initial_women = 30
    initial_men = 20
    initial_total = initial_women + initial_men
    left_percent = 2/5
    left_total = initial_total * left_percent
    left_men = 9
    left_women = left_total - left_men
    remaining_women = initial_women - left_women
    remaining_men = initial_men - left_men
    difference = remaining_women - remaining_men
    result = difference
    return result

print(solution())