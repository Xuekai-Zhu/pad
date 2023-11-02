def solution():
    """A man divides 3 hectares of land evenly among his 8 sons. If every 750m^2 of this land can be used to make a profit of $500 from every 3 months of commercial farming, how much can each son make if they cultivate their share of the land for one year(1 hectare is equal to 10000 m^2)?"""
    land_size = 3 * 10000 # convert hectares to m^2
    num_of_sons = 8
    son_share = land_size // num_of_sons
    profit_per_unit = 500
    unit_size = 750 # in m^2
    harvests_per_year = 4 # every 3 months
    total_profit_per_son = (son_share // unit_size) * profit_per_unit * harvests_per_year
    result = total_profit_per_son
    return result

print(solution())