def solution():
    # Calculate the amount Alfred needs to save each month
    remaining_amount = 100  # remaining amount from last year's holiday
    total_goal = 1000  # total amount Alfred wants to save
    months = 12  # number of months to save
    amount_per_month = (total_goal - remaining_amount) / months  # amount Alfred needs to save per month to reach his goal
    result = amount_per_month
    return result

print(solution())