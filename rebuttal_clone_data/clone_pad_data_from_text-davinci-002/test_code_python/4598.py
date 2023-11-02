def solution():
    white_men = 20
    black_men = 18
    men_total = white_men + black_men
    white_women = white_men - 5
    black_women = black_men - 5
    women_total = white_women + black_women
    total_employees = men_total + women_total
    total_cost = white_men + black_men + white_women + black_women
    
    return total_cost

print(solution())