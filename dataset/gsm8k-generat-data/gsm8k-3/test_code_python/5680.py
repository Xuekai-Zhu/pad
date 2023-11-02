def solution():
    """Ten percent of Jonessa's pay goes to paying tax. If her pay is $500, how much is her take-home pay?"""
    # Define the percentage of pay that goes to tax
    TAX_PERCENTAGE = 0.1

    # Define Jonessa's pay
    pay = 500

    # Calculate the amount of tax taken out of her pay
    tax = pay * TAX_PERCENTAGE

    # Calculate Jonessa's take-home pay
    take_home_pay = pay - tax

    # Display Jonessa's take-home pay
    result = take_home_pay
    return result

print(solution())