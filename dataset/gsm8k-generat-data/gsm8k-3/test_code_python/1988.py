def solution():
    """Jackson and Brandon both invest $500 in the stock market. Jackson's investment quadruples in value, while Brandon's is reduced to 20% of the initial value. How much more money does Jackson have than Brandon now?"""
    # Define the initial investment and changes in value for each person
    initial_investment = 500
    jackson_increase = 4
    brandon_decrease = 0.2

    # Calculate the final values of each person's investment
    jackson_final = initial_investment * jackson_increase
    brandon_final = initial_investment * brandon_decrease

    # Calculate the difference in the final values
    difference = jackson_final - brandon_final

    # Display the difference in the final values
    result = difference
    return result

print(solution())