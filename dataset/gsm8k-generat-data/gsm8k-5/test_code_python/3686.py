def solution():
    amount_given_back = 30000  # Connie gave $30,000 back to Blake
    fraction_given_back = 1/2  # Connie gave half of the money from the land sale to Blake
    amount_after_sale = amount_given_back / fraction_given_back  # Double the amount given back, since only half of the sale price was given back to Blake
    value_before_sale = amount_after_sale / 3  # The land tripled in value, so this is 1/3 of the amount after the sale
    initial_amount = amount_given_back + value_before_sale  # The initial amount Blake gave to Connie is the sum of the money given back and the value before the sale
    result = initial_amount
    return result

print(solution())