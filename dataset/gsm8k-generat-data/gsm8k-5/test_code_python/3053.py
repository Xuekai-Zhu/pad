def solution():
    weekly_savings = 25  # Carl saved $25 each week for 6 weeks
    weeks_saved = 6  # Carl saved for 6 weeks
    total_savings = weekly_savings * weeks_saved  # Total savings after 6 weeks

    # On the seventh week, Carl used 1/3 of his savings to pay bills
    total_savings -= total_savings / 3

    # Carl needed $170 to buy the coat, so his dad gave him the remaining amount
    dad_gave = 170 - total_savings

    result = dad_gave
    return result

print(solution())