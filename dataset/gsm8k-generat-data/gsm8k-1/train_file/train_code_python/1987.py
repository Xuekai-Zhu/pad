def solution():
    """Jackson and Brandon both invest $500 in the stock market. Jackson's investment quadruples in value, while Brandon's is reduced to 20% of the initial value. How much more money does Jackson have than Brandon now?"""
    initial_investment = 500
    jackson_value = initial_investment * 4
    brandon_value = initial_investment * 0.2
    difference = jackson_value - brandon_value
    result = difference
    return result

print(solution())