def solution():
     game_price = 60
     earnings = 35
     trout_price = 5
     bluegill_price = 4
     trout_percent = 60
     trout_amount = 5 * (trout_percent / 100)
     bluegill_amount = 5 - trout_amount
     trout_total = trout_price * trout_amount
     bluegill_total = bluegill_price * bluegill_amount
     total_earnings = trout_total + bluegill_total + earnings
     result = game_price - total_earnings
     return result

print(solution())