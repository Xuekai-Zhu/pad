def solution():
    total_goal = 100
    days_working = 4
    pay_per_pound = 2

    # Calculate how much Steve earned on Monday
    monday_pounds = 8
    monday_pay = monday_pounds * pay_per_pound

    # Calculate how much Steve earned on Tuesday
    tuesday_pounds = monday_pounds * 3
    tuesday_pay = tuesday_pounds * pay_per_pound

    # Calculate total earnings so far and remaining earnings needed
    total_earnings = monday_pay + tuesday_pay
    remaining_earnings = total_goal - total_earnings

    # Calculate how many pounds of lingonberries Steve needs to pick on Thursday to reach his goal
    thursday_pounds = remaining_earnings / (pay_per_pound * (days_working - 2))

    result = thursday_pounds
    return result

print(solution())