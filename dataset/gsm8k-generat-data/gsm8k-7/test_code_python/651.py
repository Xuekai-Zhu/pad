def solution():
    pay_rate = 9
    monday_hours = 4
    wednesday_hours = 3
    friday_hours = 6

    # Calculate the total number of hours that Olivia worked
    total_hours = monday_hours + wednesday_hours + friday_hours

    # Calculate the total amount of money that Olivia made this week
    total_earnings = total_hours * pay_rate
    result = total_earnings
    return result

print(solution())