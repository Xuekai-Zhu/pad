def solution():
    """At a shop in Japan, women's T-shirts are sold every 30 minutes for $18, and men's T-shirts are sold every 40 minutes for $15. This shop is open from 10 am until 10 pm. How much does the shop earn selling T-shirts per week?"""
    # Calculate the number of T-shirts sold per hour for women's and men's T-shirts
    women_tshirts_per_hour = 2 * 60 / 30 # 2 T-shirts per 30 minutes
    men_tshirts_per_hour = 2 * 60 / 40 # 2 T-shirts per 40 minutes

    # Calculate the total revenue earned per hour from women's and men's T-shirts
    women_tshirt_revenue_per_hour = women_tshirts_per_hour * 18
    men_tshirt_revenue_per_hour = men_tshirts_per_hour * 15

    # Calculate the total revenue earned per day from women's and men's T-shirts
    total_revenue_per_day = (women_tshirt_revenue_per_hour + men_tshirt_revenue_per_hour) * 12 # The shop is open for 12 hours

    # Calculate the total revenue earned per week
    total_revenue_per_week = total_revenue_per_day * 7

    # Display the total revenue earned per week
    result = total_revenue_per_week
    return result

print(solution())