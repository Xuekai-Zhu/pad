def solution():
    """At a shop in Japan, women's T-shirts are sold every 30 minutes for $18, and men's T-shirts are sold every 40 minutes for $15. This shop is open from 10 am until 10 pm. How much does the shop earn selling T-shirts per week?"""
    women_shirts_per_hour = 2
    men_shirts_per_hour = 1.5
    hours_per_day = 12
    days_per_week = 7
    price_per_women_shirt = 18
    price_per_men_shirt = 15
    total_women_shirts_sold = women_shirts_per_hour * hours_per_day * days_per_week
    total_men_shirts_sold = men_shirts_per_hour * hours_per_day * days_per_week
    total_earnings = (total_women_shirts_sold * price_per_women_shirt) + (total_men_shirts_sold * price_per_men_shirt)
    result = total_earnings
    return result

print(solution())