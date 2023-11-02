def solution():
    josh_hours = 8 * 5 * 4  # Josh works for 8 hours a day, 5 days a week, and 4 weeks a month
    carl_hours = josh_hours - 2  # Carl works 2 hours less than Josh every day
    josh_pay = 9  # Josh gets paid $9 per hour
    carl_pay = josh_pay / 2  # Carl gets paid half of what Josh makes per hour

    # Calculate the total pay for Josh and Carl in one month
    total_pay = (josh_hours * josh_pay) + (carl_hours * carl_pay)
    result = total_pay
    return result

print(solution())