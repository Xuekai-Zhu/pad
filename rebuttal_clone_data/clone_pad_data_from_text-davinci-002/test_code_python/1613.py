def solution():
    houses_per_day = 50
    percentage_of_buyers = 20
    buyers_per_day = houses_per_day * (percentage_of_buyers / 100)
    knife_set_1_sales = buyers_per_day / 2
    knife_set_2_sales = buyers_per_day / 2
    price_of_set_1 = 50
    price_of_set_2 = 150
    total_sales_per_day = (knife_set_1_sales * price_of_set_1) + (knife_set_2_sales * price_of_set_2)
    days_per_week = 5
    total_sales_per_week = total_sales_per_day * days_per_week
    result = total_sales_per_week
    return result

print(solution())