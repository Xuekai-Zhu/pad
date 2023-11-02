def solution():
    """The price of a math textbook in the school bookshop is $45. If those sold in bookshops outside the school cost 20% less, how much can Peter save by buying from other bookshops rather than the school's if he wants to buy 3 math textbooks?"""
    # Define the price of a math textbook in the school bookshop and the number of textbooks Peter wants to buy
    school_price = 45
    num_textbooks = 3

    # Calculate the percentage discount at other bookshops
    discount_percentage = 20

    # Calculate the price of a math textbook at other bookshops
    other_price = school_price * (1 - (discount_percentage/100))

    # Calculate the total cost of buying 3 math textbooks at the school bookshop
    school_total = school_price * num_textbooks

    # Calculate the total cost of buying 3 math textbooks at other bookshops
    other_total = other_price * num_textbooks

    # Calculate the amount Peter can save by buying from other bookshops
    savings = school_total - other_total

    result = savings
    return result

print(solution())