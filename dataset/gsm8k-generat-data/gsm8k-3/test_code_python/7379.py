def solution():
    """A man divides 3 hectares of land evenly among his 8 sons. If every 750m^2 of this land can be used to make a profit of $500 from every 3 months of commercial farming, how much can each son make if they cultivate their share of the land for one year(1 hectare is equal to 10000 m^2)?"""
    # Define the area of land that each son receives
    land_per_son = (3 * 10000) / 8

    # Calculate the number of 750m^2 plots that each son receives
    plots_per_son = land_per_son / 750

    # Calculate the profit that each son can make from their plots in 1 year
    profit_per_son = 4 * 500 * plots_per_son

    # Display the profit that each son can make
    result = profit_per_son
    return result

print(solution())