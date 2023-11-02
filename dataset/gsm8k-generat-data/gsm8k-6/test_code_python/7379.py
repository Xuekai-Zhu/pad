def solution():
    # Convert the 3 hectares of land to square meters
    land_area = 3 * 10000

    # Calculate the area of land each son gets
    area_per_son = land_area / 8

    # Calculate the number of 750m^2 plots each son has
    plots_per_son = area_per_son / 750

    # Calculate the profit each son can make in a year
    profit_per_son = plots_per_son * (500 / 3) * 4  # 4 quarters in a year

    result = profit_per_son
    return result

print(solution())