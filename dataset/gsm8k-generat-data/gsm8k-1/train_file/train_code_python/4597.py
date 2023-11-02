def solution():
    """Juan bought T-shirts for his employees. He bought shirts for men and women. Women's t-shirts are $5 cheaper than men's t-shirts of the same color. His company has 2 sectors, one in white t-shirts and the other in black t-shirts. He paid $20 for white men's t-shirts and $18 for black men's t-shirts. The 2 sectors have the same number of men and women, with a total of 40 employees. How much did he spend total on buying t-shirts?"""
    men_cost = (20 + 18) / 2  # average cost of men's shirts
    women_cost = men_cost - 5  # women's shirts are $5 cheaper
    total_employees = 40
    men_count = total_employees // 2
    women_count = total_employees // 2
    white_shirt_cost = (men_count * men_cost) + (women_count * women_cost)
    black_shirt_cost = (men_count * men_cost) + (women_count * women_cost)
    total_cost = white_shirt_cost + black_shirt_cost
    result = total_cost
    return result

print(solution())