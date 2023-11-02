def solution():
    """The price of a math textbook in the school bookshop is $45. If those sold in bookshops outside the school cost 20%
    less, how much can Peter save by buying from other bookshops rather than the school's if he wants to buy 3 math textbooks?"""
    school_price = 45
    discount_percent = 20
    outside_price = school_price - (school_price * (discount_percent / 100))
    total_cost = 3 * outside_price
    savings = (3 * school_price) - total_cost
    result = savings
    return result

print(solution())