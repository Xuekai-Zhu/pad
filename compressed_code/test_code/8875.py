def solution():
    
    current_speed = 10
    current_bill = 20
    faster_speed = 30
    faster_price = current_bill * 2
    slower_speed = 20
    slower_price = current_bill + 10

    
    annual_cost_faster = faster_price * 12

    
    annual_cost_slower = slower_price * 12

    
    annual_savings = annual_cost_faster - annual_cost_slower
    result = annual_savings
    return result

print(solution())