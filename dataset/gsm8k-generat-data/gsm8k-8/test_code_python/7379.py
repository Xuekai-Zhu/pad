def solution():
    # Convert 3 hectares to square meters
    total_area = 3 * 10000

    # Calculate the area of land each son gets
    son_area = total_area / 8

    # Calculate the number of 750m^2 areas in each son's land
    num_areas = son_area / 750

    # Calculate the profit each son can make in a year
    annual_profit = num_areas * 500 * 4

    # Divide the annual profit equally among the 8 sons
    son_profit = annual_profit / 8
    result = son_profit
    return result

print(solution())