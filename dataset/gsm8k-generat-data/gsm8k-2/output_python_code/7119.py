def solution():
    """Adam's father deposited $2000 in the bank. It receives 8% interest paid throughout the year, and he withdraws the interest as soon as it is deposited. How much will Adam’s father have, including his deposit and the interest received after 2 and a half years?"""
    deposit = 2000
    interest_rate = 0.08
    time_in_years = 2.5
    total_interest = deposit * interest_rate * time_in_years
    total_amount = deposit + total_interest
    result = total_amount
    return result

print(solution())