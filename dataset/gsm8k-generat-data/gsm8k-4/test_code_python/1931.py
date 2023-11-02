def solution():
    """At a shop in Japan, women's T-shirts are sold every 30 minutes for $18, and men's T-shirts are sold every 40 minutes for $15. This shop is open from 10 am until 10 pm. How much does the shop earn selling T-shirts per week?"""
    # Define the prices and selling times for women's and men's T-shirts
    women_price = 18
    women_time = 30
    men_price = 15
    men_time = 40

    # Calculate the number of T-shirts sold in one day for women and men separately
    women_shirts_per_day = (12*60 // women_time) * 2
    men_shirts_per_day = (12*60 // men_time) * 2

    # Calculate the total earnings per day
    total_earnings_per_day = women_price * women_shirts_per_day + men_price * men_shirts_per_day

    # Calculate the total earnings per week
    total_earnings_per_week = total_earnings_per_day * 7

    # Return the result
    result = total_earnings_per_week
    return result

print(solution())