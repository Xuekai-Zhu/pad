def solution():
    """The price of a math textbook in the school bookshop is $45. If those sold in bookshops outside the school cost 20% less, how much can Peter save by buying from other bookshops rather than the school's if he wants to buy 3 math textbooks?"""
    # Define the price of the textbook in the school bookshop
    SCHOOL_PRICE = 45

    # Calculate the price of a textbook outside the school
    OUTSIDE_PRICE = SCHOOL_PRICE * 0.8

    # Calculate the total cost of buying 3 textbooks from the school bookshop
    school_total_cost = 3 * SCHOOL_PRICE

    # Calculate the total cost of buying 3 textbooks from outside the school bookshop
    outside_total_cost = 3 * OUTSIDE_PRICE

    # Calculate how much Peter can save by buying from outside the school
    savings = school_total_cost - outside_total_cost

    # Display Peter's savings
    result = savings
    return result

print(solution())