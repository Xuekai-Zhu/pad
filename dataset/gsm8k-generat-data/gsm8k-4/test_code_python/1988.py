def solution():
    """Jackson and Brandon both invest $500 in the stock market. Jackson's investment quadruples in value, while Brandon's is reduced to 20% of the initial value. How much more money does Jackson have than Brandon now?"""
    # Define the initial investments of Jackson and Brandon
    jackson_investment = 500
    brandon_investment = 500

    # Calculate the current value of Jackson's investment
    jackson_value = jackson_investment * 4

    # Calculate the current value of Brandon's investment
    brandon_value = brandon_investment * 0.2

    # Calculate the difference in value between Jackson and Brandon's investments
    difference = jackson_value - brandon_value

    # Return the result
    result = difference
    return result

print(solution())