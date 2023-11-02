def solution():
    
    total_apples = 60
    eaten_apples = total_apples * (2/5)
    remaining_apples = total_apples - eaten_apples
    sister_apples = remaining_apples * 0.25
    remaining_apples -= sister_apples
    uncle_price = 3
    money_received = remaining_apples * uncle_price
    result = money_received
    return result

print(solution())