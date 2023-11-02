def solution():
    initial_investment = 500

    # Calculate the value of Jackson's investment after quadrupling
    jackson_value = initial_investment * 4

    # Calculate the value of Brandon's investment after being reduced to 20%
    brandon_value = initial_investment * 0.2

    # Calculate the difference between Jackson's and Brandon's current values
    difference = jackson_value - brandon_value
    result = difference
    return result

print(solution())