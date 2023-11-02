def solution():
    principle = 2000
    interest_rate = 0.08  # 8% interest
    time_in_years = 2.5

    # Calculate the total interest earned over 2.5 years
    total_interest = principle * interest_rate * time_in_years

    # Add the interest to the principle to get the total amount at the end of 2.5 years
    total_amount = principle + total_interest
    result = total_amount
    return result

print(solution())