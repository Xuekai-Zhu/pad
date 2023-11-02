def solution():
     regular_hours = 40
     first_week_hours = 44
     second_week_hours = 48
     first_week_regular_pay = 5 * regular_hours
     first_week_overtime_pay = 6 * (first_week_hours - regular_hours)
     second_week_regular_pay = 5 * regular_hours
     second_week_overtime_pay = 6 * (second_week_hours - regular_hours)
     total_pay = first_week_regular_pay + first_week_overtime_pay + second_week_regular_pay + second_week_overtime_pay
     result = total_pay
     return result

print(solution())