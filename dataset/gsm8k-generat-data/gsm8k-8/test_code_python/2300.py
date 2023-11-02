def solution():
    # Calculate Josh's total work hours in a month
    josh_hours = 8 * 5 * 4

    # Calculate Carl's total work hours in a month
    carl_hours = (8-2) * 5 * 4

    # Calculate Josh's total pay in a month
    josh_pay = josh_hours * 9

    # Calculate Carl's total pay in a month
    carl_pay = carl_hours * 4.5

    # Calculate the total pay for both of them
    total_pay = josh_pay + carl_pay
    result = total_pay
    return result

print(solution())