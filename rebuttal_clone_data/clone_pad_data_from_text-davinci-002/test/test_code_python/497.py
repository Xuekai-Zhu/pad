def solution():
     cups_brewed_hourly = 10
     cups_brewed_weekend = 120
     cups_brewed_daily = cups_brewed_hourly * 5
     cups_brewed_weekly = cups_brewed_daily * 5 + cups_brewed_weekend
     result = cups_brewed_weekly
     return result

print(solution())