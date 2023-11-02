def solution():
    total_land = 3 * 10000  # Convert 3 hectares to square meters
    num_sons = 8
    land_per_son = total_land / num_sons

    # Calculate the profit per son for 3 months
    profit_per_period = (750 / 10000) * 500  # Convert 750m^2 to hectares
    periods_per_year = 4  # There are 4 three-month periods in a year
    profit_per_year = profit_per_period * periods_per_year

    # Calculate the profit per son for one year
    profit_per_son = profit_per_year * (land_per_son / 1)

    result = profit_per_son
    return result

print(solution())