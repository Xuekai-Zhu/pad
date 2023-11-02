def solution():
    original_amount = 300  # Brenda invested $300 into the scheme
    interest_rate = 3/4  # The rate of interest is three-quarters of the original amount per year
    years = 3  # Brenda wants to know how much she will have after 3 years

    # Calculate the total amount Brenda will have after 3 years
    total_amount = original_amount * (1 + interest_rate) * years
    result = total_amount
    return result

print(solution())