def solution():
    """Juan bought T-shirts for his employees. He bought shirts for men and women. Women's t-shirts are $5 cheaper than men's t-shirts of the same color. His company has 2 sectors, one in white t-shirts and the other in black t-shirts. He paid $20 for white men's t-shirts and $18 for black men's t-shirts. The 2 sectors have the same number of men and women, with a total of 40 employees. How much did he spend total on buying t-shirts?"""
    white_men_shirt = 20
    black_men_shirt = 18
    white_women_shirt = white_men_shirt - 5
    black_women_shirt = black_men_shirt - 5
    total_employees = 40
    men_employees = total_employees // 2
    women_employees = total_employees // 2
    white_shirts_cost = (white_men_shirt + white_women_shirt) * men_employees + (white_women_shirt + white_men_shirt) * women_employees
    black_shirts_cost = (black_men_shirt + black_women_shirt) * men_employees + (black_women_shirt + black_men_shirt) * women_employees
    total_cost = white_shirts_cost + black_shirts_cost
    result = total_cost
    return result

print(solution())