def solution():
     carls_earnings = 0.50
     money_from_neighbor = 0.75
     carls_earnings_per_week = carls_earnings + money_from_neighbor
     candy_bars_per_week = carls_earnings_per_week / 0.50
     candy_bars_total = candy_bars_per_week * 4
     result = candy_bars_total
     return result

print(solution())