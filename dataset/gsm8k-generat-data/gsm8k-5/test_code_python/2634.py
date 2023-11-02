def solution():
    textbook_price = 45  # Price of a math textbook in the school bookshop
    discount_percent = 20  # Discount percentage for bookshops outside the school
    discount_amount = discount_percent / 100 * textbook_price  # Calculate the discount amount
    discounted_price = textbook_price - discount_amount  # Calculate the discounted price
    num_textbooks = 3  # Peter wants to buy 3 math textbooks

    # Calculate the total cost of buying from the school bookshop
    school_cost = textbook_price * num_textbooks

    # Calculate the total cost of buying from other bookshops
    other_cost = discounted_price * num_textbooks

    # Calculate the amount Peter can save by buying from other bookshops
    savings = school_cost - other_cost

    result = savings
    return result

print(solution())