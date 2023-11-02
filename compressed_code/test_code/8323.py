def solution():
    
    computers_per_day = 1500
    days_per_week = 7
    price_per_computer = 150
    total_computers = computers_per_day * days_per_week
    total_money = total_computers * price_per_computer
    result = total_money
    return result

print(solution())