def solution():
    num_plain_lemonades = 36
    plain_lemonade_price = 0.75
    total_strawberry_lemonade_income = 16

    # Calculate the total income from plain lemonade
    plain_lemonade_income = num_plain_lemonades * plain_lemonade_price

    # Calculate the income difference between plain and strawberry lemonade
    income_difference = plain_lemonade_income - total_strawberry_lemonade_income
    result = income_difference
    return result

print(solution())