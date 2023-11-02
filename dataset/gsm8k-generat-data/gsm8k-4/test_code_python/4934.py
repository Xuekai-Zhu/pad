def solution():
    """Emma and Briana invested some capital into a business. Emma's investment is supposed to yield 15% of the capital annually while Briana's should yield 10% annually. If Emma invested $300 and Briana invested $500, what will be the difference between their return-on-investment after 2 years?"""
    # Define the initial investments and the annual interest rates
    emma_investment = 300
    briana_investment = 500
    emma_interest_rate = 0.15
    briana_interest_rate = 0.10

    # Calculate Emma's return on investment after 2 years
    emma_roi = emma_investment * (1 + emma_interest_rate)**2

    # Calculate Briana's return on investment after 2 years
    briana_roi = briana_investment * (1 + briana_interest_rate)**2

    # Calculate the difference between their returns on investment
    difference = emma_roi - briana_roi

    # return the result
    result = difference
    return result

print(solution())