def solution():
    """Tim and Donna will celebrate their 20th wedding anniversary in 2025. They started dating 3 years before they got married and met 2 years before that. When did they meet?"""
    anniversary_year = 2025
    years_married = 20
    years_dating = 3
    years_known = 2
    year_they_met = anniversary_year - years_married - years_dating - years_known
    result = year_they_met
    return result

print(solution())