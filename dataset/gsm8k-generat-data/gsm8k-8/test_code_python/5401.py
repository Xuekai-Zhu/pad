def solution():
    # Define the initial amount Lyka has and the total amount she needs to save
    initial_amount = 40
    total_amount = 160 - initial_amount

    # Calculate the number of weeks in two months and round up to ensure full weeks
    num_weeks = math.ceil(2 * 4.35)

    # Calculate the amount Lyka needs to save per week
    weekly_savings = total_amount / num_weeks
    result = weekly_savings
    return result

print(solution())