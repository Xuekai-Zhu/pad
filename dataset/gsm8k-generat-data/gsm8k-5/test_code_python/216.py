def solution():
    total_amount = 450  # The bank contained $450 in change
    years = 4  # The piggy bank was saved for 4 years
    amount_last_year = total_amount / ((2**3) + 1)  # Missy doubled the amount every year after the first year
    amount_first_year = amount_last_year / 2  # The amount in the first year is half the amount in the second year
    result = amount_first_year
    return result

print(solution())