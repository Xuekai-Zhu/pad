def solution():
    lemonade_sold_week_1 = 20
    percent_increase = 30
    lemonade_sold_week_2 = lemonade_sold_week_1 + (lemonade_sold_week_1 * (percent_increase / 100))
    total_lemonade_sold = lemonade_sold_week_1 + lemonade_sold_week_2
    result = total_lemonade_sold
    return result

print(solution())