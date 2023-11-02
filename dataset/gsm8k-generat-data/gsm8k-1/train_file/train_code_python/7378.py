def solution():
    """A man divides 3 hectares of land evenly among his 8 sons. If every 750m² of this land can be used to make a profit of $500 from every 3 months of commercial farming, how much can each son make if they cultivate their share of the land for one year(1 hectare is equal to 10000 m²)?"""
    total_land = 3 * 10000
    sons = 8
    land_per_son = total_land / sons
    profit_per_750m2 = 500
    area_per_profit = 750
    profits_per_hectare = (land_per_son / area_per_profit) * profit_per_750m2 * 4 # four for year
    profits_per_son = profits_per_hectare * 3 # three hectares per son
    result = profits_per_son
    return result

print(solution())