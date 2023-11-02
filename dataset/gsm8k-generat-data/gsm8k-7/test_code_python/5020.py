def solution():
    total_sales = 2500
    commission_rate = 0.02
    basic_salary = 240
    saving_rate = 0.1

    # Calculate the amount of commission Alice will receive
    commission = total_sales * commission_rate

    # Calculate Alice's total earnings
    total_earnings = basic_salary + commission

    # Calculate the amount of money Alice will save
    savings = total_earnings * saving_rate
    result = savings
    return result

print(solution())