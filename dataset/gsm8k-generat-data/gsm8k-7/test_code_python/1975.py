def solution():
    initial_amount = 1000
    first_year_interest = 0.2
    second_year_interest = 0.15

    # Calculate the amount after the first year with interest
    amount_after_first_year = initial_amount * (1 + first_year_interest)

    # Calculate the amount after taking out half to buy a new TV
    remaining_amount = amount_after_first_year / 2

    # Calculate the amount after the second year with interest
    amount_after_second_year = remaining_amount * (1 + second_year_interest)

    result = amount_after_second_year
    return result

print(solution())