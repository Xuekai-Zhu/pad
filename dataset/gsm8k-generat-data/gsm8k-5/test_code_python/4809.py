def solution():
    principal = 200  # Jerry owes a loan shark $200
    interest_rate = 0.1  # The loan shark charges 10% interest compounded monthly
    months = 2  # We want to calculate the interest charged in the second month

    # Calculate the interest charged in the first month
    interest_first_month = principal * (interest_rate / 12)

    # Calculate the new total (including interest) after the first month
    total_first_month = principal + interest_first_month

    # Calculate the interest charged in the second month
    interest_second_month = total_first_month * (interest_rate / 12)

    result = interest_second_month
    return result

print(solution())