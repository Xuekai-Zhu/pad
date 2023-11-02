def solution():
    hourly_rate = 10
    mon_hours = 7
    mon_tips = 18
    tue_hours = 5
    tue_tips = 12
    wed_hours = 7
    wed_tips = 20

    mon_pay = hourly_rate * mon_hours
    tue_pay = hourly_rate * tue_hours
    wed_pay = hourly_rate * wed_hours
    total_tips = mon_tips + tue_tips + wed_tips

    total_earnings = mon_pay + tue_pay + wed_pay + total_tips
    result = total_earnings
    return result

print(solution())