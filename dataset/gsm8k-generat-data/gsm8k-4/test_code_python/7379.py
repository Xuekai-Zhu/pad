def solution():
    """A man divides 3 hectares of land evenly among his 8 sons. If every 750m^2 of this land can be used to make a profit of $500 from every 3 months of commercial farming, how much can each son make if they cultivate their share of the land for one year(1 hectare is equal to 10000 m^2)?"""
    # Define the total area of land in m^2
    total_area = 3 * 10000

    # Calculate the area of land per son in m^2
    area_per_son = total_area / 8

    # Calculate the number of 750m^2 plots for each son
    plots_per_son = area_per_son / 750

    # Calculate the profit per son for 1 year
    profit_per_son = plots_per_son * 500 * 4

    result = profit_per_son
    return result

print(solution())