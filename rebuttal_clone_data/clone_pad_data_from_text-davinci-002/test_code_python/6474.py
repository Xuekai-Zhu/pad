def solution():
    bottles_sold_A = 300
    bottles_sold_B = 350
    price_A = 4
    price_B = 3.5
    total_revenue_A = bottles_sold_A * price_A
    total_revenue_B = bottles_sold_B * price_B
    difference = total_revenue_A - total_revenue_B
    result = difference
    return result

print(solution())