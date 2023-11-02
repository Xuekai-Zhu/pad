def solution():
    # Define the variables
    month1_days = 30
    month2_days = 30
    month3_days = 15
    month1_pay = 10
    month2_pay = 2 * month1_pay
    month3_pay = month2_pay

    # Calculate the total pay for each month
    month1_total_pay = month1_days * month1_pay
    month2_total_pay = month2_days * month2_pay
    month3_total_pay = month3_days * month3_pay

    # Calculate the total pay for all three months
    total_pay = month1_total_pay + month2_total_pay + month3_total_pay
    result = total_pay
    return result

print(solution())