def solution():
    # Define the initial amount in Emma's bank account
    initial_amount = 100

    # Define the amount spent each day
    daily_spending = 8

    # Calculate the total amount spent in a week
    total_spending = daily_spending * 7

    # Calculate the remaining amount in the account after a week of spending
    remaining_amount = initial_amount - total_spending

    # Calculate the number of $5 bills that can be withdrawn from the remaining amount
    num_five_bills = remaining_amount // 5

    # Calculate the final remaining amount in the account
    final_amount = remaining_amount - (num_five_bills * 5)

    result = final_amount
    return result

print(solution())