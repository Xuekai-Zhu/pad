def solution():
    hourly_wage = 10
    hours_worked_Monday = 7
    tips_earned_Monday = 18
    hours_worked_Tuesday = 5
    tips_earned_Tuesday = 12
    hours_worked_Wednesday = 7
    tips_earned_Wednesday = 20
    total_tips = tips_earned_Monday + tips_earned_Tuesday + tips_earned_Wednesday
    total_hours = hours_worked_Monday + hours_worked_Tuesday + hours_worked_Wednesday
    total_earnings = total_hours * hourly_wage + total_tips
    result = total_earnings
    return result

print(solution())