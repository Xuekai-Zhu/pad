def solution():
    """Aaron pays his actuary membership fees each year. The membership fee increases yearly by $10. If he pays $80 in the first year, how much does his membership cost, in dollars, in the sixth year?"""
    # Define the initial membership fee and the annual increase
    initial_fee = 80
    annual_increase = 10

    # Calculate the membership fee in the sixth year
    sixth_year_fee = initial_fee + (annual_increase * 5)

    # Display the membership fee in the sixth year
    result = sixth_year_fee
    return result

print(solution())