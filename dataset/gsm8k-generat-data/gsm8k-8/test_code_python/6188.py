def solution():
    # Calculate the total earnings from each job
    job1_earnings = 20 * 10
    job2_earnings = 30 * 20
    job3_earnings = 5 * 40

    # Calculate the total earnings and expenses for the month
    total_earnings = job1_earnings + job2_earnings + job3_earnings
    total_expenses = 500

    # Calculate the money left at the end of the month
    money_left = total_earnings - total_expenses
    result = money_left
    return result

print(solution())