def solution():
     organic_egg_price = 0.50
     tray_price = 12
     tray_size = 30
     egg_price_from_tray = tray_price / tray_size
     cost_savings = egg_price_from_tray - organic_egg_price
     result = cost_savings
     return result

print(solution())