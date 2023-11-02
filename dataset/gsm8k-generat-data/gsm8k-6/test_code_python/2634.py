def solution():
    textbook_price_school = 45  # price of textbook in school bookshop
    textbook_price_outside = textbook_price_school * 0.8  # price of textbook outside school bookshop
    n_textbooks = 3  # number of textbooks Peter wants to buy

    # Calculate the total cost of buying 3 textbooks from the school bookshop
    cost_school = textbook_price_school * n_textbooks

    # Calculate the total cost of buying 3 textbooks from an outside bookshop
    cost_outside = textbook_price_outside * n_textbooks

    # Calculate the amount Peter can save by buying from an outside bookshop
    amount_saved = cost_school - cost_outside
    result = amount_saved
    return result

print(solution())