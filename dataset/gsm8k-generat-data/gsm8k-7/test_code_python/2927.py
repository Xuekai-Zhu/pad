def solution():
    current_monthly_sales = 4000
    yearly_goal = 60000

    # Calculate the total sales needed to reach the yearly goal
    total_sales_needed = yearly_goal - (current_monthly_sales * 12)

    # Calculate the additional monthly sales needed to reach the yearly goal
    additional_monthly_sales = total_sales_needed / 12
    result = additional_monthly_sales
    return result

print(solution())