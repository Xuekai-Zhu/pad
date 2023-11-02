def solution():
     dimes = 19
     quarters = 6
     candy_bars = 3
     lollipops = 1
     remaining_dimes = dimes - (candy_bars * 4)
     remaining_quarters = quarters - lollipops
     remaining_cents = (remaining_dimes * 10) + (remaining_quarters * 25)
     result = remaining_cents
     return result

print(solution())