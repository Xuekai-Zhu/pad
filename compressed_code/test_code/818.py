def solution():
    
  
    doll_price = 5
    clock_price = 15
    glass_price = 4
    dolls = 3
    clocks = 2
    glasses = 5
    total_spent = 40
    total_profit = (doll_price * dolls) + (clock_price * clocks) + (glass_price * glasses) - total_spent
    result = total_profit
    return result

print(solution())