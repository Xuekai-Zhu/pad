def solution():
    
    initial_cost = 300
    selling_price = 255
    loss = initial_cost - selling_price
    loss_percentage = (loss / initial_cost) * 100
    result = loss_percentage
    return result

print(solution())