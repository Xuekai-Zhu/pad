def solution():
    emma_investment = 300
    emma_rate = 0.15
    briana_investment = 500
    briana_rate = 0.1
    num_years = 2

    # Calculate the return-on-investment for Emma after 2 years
    emma_roi = emma_investment * ((1 + emma_rate) ** num_years) - emma_investment

    # Calculate the return-on-investment for Briana after 2 years
    briana_roi = briana_investment * ((1 + briana_rate) ** num_years) - briana_investment

    # Calculate the difference between their return-on-investment
    difference = abs(emma_roi - briana_roi)
    result = difference
    return result

print(solution())