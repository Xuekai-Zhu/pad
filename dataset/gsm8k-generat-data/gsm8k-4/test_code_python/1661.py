def solution():
    """Tim and Donna will celebrate their 20th wedding anniversary in 2025. They started dating 3 years before they got married and met 2 years before that. When did they meet?"""
    # Define the year of their 20th wedding anniversary
    anniversary_year = 2025

    # Calculate the year they got married
    married_year = anniversary_year - 20

    # Calculate the year they started dating
    dating_year = married_year - 3

    # Calculate the year they met
    met_year = dating_year - 2

    result = met_year
    return result

print(solution())