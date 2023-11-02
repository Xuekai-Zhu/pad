def solution():
    """Aaron pays his actuary membership fees each year. The membership fee increases yearly by $10. If he pays $80 in the first year, how much does his membership cost, in dollars, in the sixth year?"""
    # Define the initial membership fee and the annual fee increase
    INITIAL_FEE = 80
    ANNUAL_INCREASE = 10

    # Calculate the membership fee in the sixth year
    sixth_year_fee = INITIAL_FEE + (ANNUAL_INCREASE * 5)

    # Return the result
    result = sixth_year_fee
    return result

print(solution())