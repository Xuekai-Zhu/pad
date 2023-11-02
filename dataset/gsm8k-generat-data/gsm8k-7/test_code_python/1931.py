def solution():
    women_shirts_price = 18
    men_shirts_price = 15
    women_shirts_interval = 30  # in minutes
    men_shirts_interval = 40  # in minutes
    shop_open_time = 12  # in hours
    days_per_week = 7
    
    # Calculate the total number of women's T-shirts sold per hour
    women_shirts_per_hour = 60 // women_shirts_interval

    # Calculate the total number of men's T-shirts sold per hour
    men_shirts_per_hour = 60 // men_shirts_interval

    # Calculate the number of hours the shop is open per day
    hours_open_per_day = shop_open_time - 10

    # Calculate the total earnings from women's T-shirts per day
    women_shirts_earnings_per_day = women_shirts_price * women_shirts_per_hour * hours_open_per_day

    # Calculate the total earnings from men's T-shirts per day
    men_shirts_earnings_per_day = men_shirts_price * men_shirts_per_hour * hours_open_per_day

    # Calculate the total earnings per day
    total_earnings_per_day = women_shirts_earnings_per_day + men_shirts_earnings_per_day

    # Calculate the total earnings per week
    total_earnings_per_week = total_earnings_per_day * days_per_week
    result = total_earnings_per_week
    return result

print(solution())