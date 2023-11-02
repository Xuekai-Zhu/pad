def solution():
    total_land = 3 * 10000  # convert hectares to square meters
    num_sons = 8
    land_per_son = total_land / num_sons

    profit_per_square_meter = 500 / (750 * 3)  # profit per square meter per quarter
    profit_per_year = profit_per_square_meter * land_per_son * 4  # profit per son per year

    result = profit_per_year
    return round(result, 2)

print(solution())