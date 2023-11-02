def solution():
    """Emma and Briana invested some capital into a business. Emma's investment is supposed to yield 15% of the capital annually while Briana's should yield 10% annually. If Emma invested $300 and Briana invested $500, what will be the difference between their return-on-investment after 2 years?"""
    # Define the annual return rates
    EMMA_RATE = 0.15
    BRIANA_RATE = 0.10

    # Define the initial investments
    emma_investment = 300
    briana_investment = 500

    # Calculate the returns after 2 years
    emma_return = emma_investment * (1 + EMMA_RATE)**2 - emma_investment
    briana_return = briana_investment * (1 + BRIANA_RATE)**2 - briana_investment

    # Calculate the difference between the returns
    roi_difference = abs(emma_return - briana_return)

    # Display the difference in return-on-investment
    result = roi_difference
    return result

print(solution())