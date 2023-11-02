def solution():
    men_shirts_total_cost = (20 + 18) * 20 / 2  # cost of men's shirts for both sectors, assuming same number of men in each
    women_white_shirts_cost = (20 - 5) * 10  # cost of women's white shirts, assuming 10 women in each sector
    women_black_shirts_cost = (18 - 5) * 10  # cost of women's black shirts, assuming 10 women in each sector
    total_cost = men_shirts_total_cost + women_white_shirts_cost + women_black_shirts_cost
    result = total_cost
    return result

print(solution())