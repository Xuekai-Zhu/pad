def solution():
    fixed_allowance = 20  # Carol gets a fixed $20 allowance each week
    total_earnings = 425  # Carol earned a total of $425 over 10 weeks
    variable_earnings = total_earnings - (fixed_allowance * 10)  # Calculate the total amount earned from doing extra chores
    extra_chore_payments = variable_earnings / 10  # Calculate the average extra chore payment per week

    # Calculate the average number of extra chores done each week
    avg_extra_chores = extra_chore_payments / 1.5
    result = avg_extra_chores
    return result

print(solution())