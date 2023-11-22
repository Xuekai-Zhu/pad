def solution():
    
    gas_price = 3.00
    cashback_per_gallon = 0.20
    gallons_bought = 10
    total_cost = gas_price * gallons_bought
    total_reward = total_cost - cashback_per_gallon
    result = total_reward
    return result

print(solution())