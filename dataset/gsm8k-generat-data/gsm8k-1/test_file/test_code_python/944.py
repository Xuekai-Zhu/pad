def solution():
    """Cayley markets various newspapers to get a commission on each copy sold. He gets a 10% commission on each copy of the New York Times and an 8% commission on each of the Wall Street Journal. How much commission will he earn in total from the sales of 6 copies of the New York Times and 10 copies of Wall Street Journal if each costs $5 and $15 respectively?"""
    ny_times_price = 5
    wsj_price = 15
    ny_times_sales = 6
    wsj_sales = 10
    ny_times_commission = ny_times_price * 0.1
    wsj_commission = wsj_price * 0.08
    total_commission = (ny_times_commission * ny_times_sales) + (wsj_commission * wsj_sales)
    result = total_commission
    return result

print(solution())