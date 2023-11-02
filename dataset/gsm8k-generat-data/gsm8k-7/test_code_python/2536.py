def solution():
    num_postcards_per_day = 30
    income_per_postcard = 5
    num_days = 6

    # Calculate the total number of postcards that Tina made in 6 days
    total_postcards = num_postcards_per_day * num_days

    # Calculate the total income earned by selling all the postcards
    total_income = total_postcards * income_per_postcard
    result = total_income
    return result

print(solution())