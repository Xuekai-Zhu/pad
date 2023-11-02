def solution():
    # Calculate Rhett's salary after taxes
    salary_after_tax = 5000 * 0.9

    # Calculate the total cost of the late rent payments
    total_late_rent = 2 * 1000  # assuming each monthly rent payment is $1000

    # Calculate the amount Rhett can use from his next month's salary to pay the late rent
    amount_to_pay = 3/5 * salary_after_tax

    # Calculate the remaining salary after paying the late rent
    remaining_salary = salary_after_tax - amount_to_pay

    # Calculate Rhett's monthly expense on rent
    rent_expense = (total_late_rent + amount_to_pay) / 3

    result = rent_expense
    return result

print(solution())