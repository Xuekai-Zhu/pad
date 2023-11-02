def solution():
    # Calculate the total number of hours worked by Josh in a month
    josh_hours = 8 * 5 * 4  # 8 hours a day, 5 days a week, 4 weeks a month
    # Calculate the total number of hours worked by Carl in a month
    carl_hours = (8 - 2) * 5 * 4  # Carl works 2 hours less than Josh every day
    # Calculate the total amount paid to Josh in a month
    josh_pay = josh_hours * 9  # Josh gets $9 an hour
    # Calculate the total amount paid to Carl in a month
    carl_pay = carl_hours * 4.5  # Carl gets half of Josh's pay per hour
    # Calculate the total amount paid to both Josh and Carl in a month
    total_pay = josh_pay + carl_pay
    result = total_pay
    return result

print(solution())