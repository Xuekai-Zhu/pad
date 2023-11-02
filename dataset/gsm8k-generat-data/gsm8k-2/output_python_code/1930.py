def solution():
    """At a shop in Japan, women's T-shirts are sold every 30 minutes for $18, and men's T-shirts are sold every 40 minutes for $15. This shop is open from 10 am until 10 pm. How much does the shop earn selling T-shirts per week?"""
    women_price = 18
    women_time_interval = 30
    men_price = 15
    men_time_interval = 40
    total_weekly_income = 0
    for day in range(7):
        for hour in range(10, 22):
            for minute in range(0, 60):
                if (minute % women_time_interval == 0) and (hour != 21 or minute != 30):
                    total_weekly_income += women_price
                if (minute % men_time_interval == 0) and (hour != 20 or minute != 40):
                    total_weekly_income += men_price

    result = total_weekly_income * 2  # multiplied by 2 as there are both women's and men's T-shirts
    return result

print(solution())