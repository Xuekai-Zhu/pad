def solution():
    # Calculate the number of women's T-shirts sold per day
    women_tshirts_per_day = 2 * 12  # 2 sales every hour for 12 hours
    women_tshirts_per_week = 7 * women_tshirts_per_day

    # Calculate the number of men's T-shirts sold per day
    men_tshirts_per_day = 3 * 12  # 3 sales every 2 hours for 12 hours
    men_tshirts_per_week = 7 * men_tshirts_per_day

    # Calculate the total earnings per week
    total_earnings_per_week = women_tshirts_per_week * 18 + men_tshirts_per_week * 15
    result = total_earnings_per_week
    return result

print(solution())