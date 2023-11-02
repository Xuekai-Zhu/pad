def solution():
    """Ten percent of Jonessa's pay goes to paying tax. If her pay is $500, how much is her take-home pay?"""
    # Define Jonessa's pay and tax rate
    pay = 500
    tax_rate = 0.1

    # Calculate the amount of tax
    tax = pay * tax_rate

    # Calculate Jonessa's take-home pay
    take_home_pay = pay - tax

    # Return the result
    result = take_home_pay
    return result

print(solution())