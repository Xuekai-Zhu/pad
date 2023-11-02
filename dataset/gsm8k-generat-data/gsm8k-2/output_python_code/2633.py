def solution():
    """The price of a math textbook in the school bookshop is $45. If those sold in bookshops outside the school cost 20% less, how much can Peter save by buying from other bookshops rather than the school's if he wants to buy 3 math textbooks?"""
    school_price = 45
    outside_price = school_price * 0.8
    num_textbooks = 3
    school_total = school_price * num_textbooks
    outside_total = outside_price * num_textbooks
    amount_saved = school_total - outside_total
    result = amount_saved
    return result

print(solution())