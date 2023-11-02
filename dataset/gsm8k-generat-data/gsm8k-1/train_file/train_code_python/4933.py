def solution():
    """Emma and Briana invested some capital into a business. Emma's investment is supposed to yield 15% of the capital annually while Briana's should yield 10% annually. If Emma invested $300 and Briana invested $500, what will be the difference between their return-on-investment after 2 years?"""
    emma_investment = 300
    briana_investment = 500
    emma_roi = emma_investment * 0.15 * 2
    briana_roi = briana_investment * 0.1 * 2
    difference = emma_roi - briana_roi
    result = difference
    return result

print(solution())