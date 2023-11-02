def solution():
    investment = 300  # The initial investment is $300
    months = 2  # The investment is for 2 months
    interest_rate = 0.10  # The interest rate is 10% per month

    # Calculate the total amount at the end of two months
    total_amount = investment * (1 + interest_rate)**months

    result = total_amount
    return result

print(solution())