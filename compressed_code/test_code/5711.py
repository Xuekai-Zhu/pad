def solution():
    
    land_size = 3 * 10000 
    num_of_sons = 8
    son_share = land_size // num_of_sons
    profit_per_unit = 500
    unit_size = 750 
    harvests_per_year = 4 
    total_profit_per_son = (son_share // unit_size) * profit_per_unit * harvests_per_year
    result = total_profit_per_son
    return result

print(solution())