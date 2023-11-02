def solution():
    # Define the amount of money Steve wants to make and the rate of pay per pound of berries
    target_income = 100
    pay_rate = 2

    # Calculate the amount of money earned on Monday
    monday_pounds = 8
    monday_income = monday_pounds * pay_rate

    # Calculate the amount of money earned on Tuesday
    tuesday_pounds = monday_pounds * 3
    tuesday_income = tuesday_pounds * pay_rate

    # Calculate the total amount of money earned so far
    total_income = monday_income + tuesday_income

    # Calculate the amount of money still needed to reach the target income
    remaining_income = target_income - total_income

    # Calculate the pounds of lingonberries needed to make the remaining income
    pounds_needed = remaining_income / pay_rate
    result = pounds_needed
    return result

print(solution())