def solution():
    """Jackson and Brandon both invest $500 in the stock market. Jackson's investment quadruples in value, while Brandon's is reduced to 20% of the initial value. How much more money does Jackson have than Brandon now?"""
    jackson_investment = 500 * 4
    brandon_investment = 500 * 0.2
    difference = jackson_investment - brandon_investment
    result = difference
    return result

print(solution())