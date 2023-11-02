def solution():
    hourly_wage = 50
    hours_worked = 10
    percent_withheld = 20
    money_withheld = (hourly_wage * hours_worked) * (percent_withheld / 100)
    money_received = (hourly_wage * hours_worked) - money_withheld
    result = money_received
 
    return result

print(solution())