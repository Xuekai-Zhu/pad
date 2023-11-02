def solution():
    # Calculate the interest earned in the first year
    first_year_interest = 0.07 * 5600  # 7% of $5600

    # Calculate the total amount in the account after the first year
    first_year_total = 5600 + first_year_interest

    # Calculate the interest earned in the second year
    second_year_interest = 0.07 * first_year_total

    # Calculate the total amount in the account after two years
    total_amount = first_year_total + second_year_interest
    result = total_amount
    return result

print(solution())