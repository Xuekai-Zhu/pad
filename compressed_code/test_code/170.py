def solution():
    
    total_cost = 4.20 + 2.05
    payment = 7.00
    change = payment - total_cost
    nickels = int((change - 0.25 - 0.10) / 0.05)
    result = nickels
    return result

print(solution())