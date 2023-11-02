def solution():
    
    apples_price = 200 / 10 
    oranges_price = 150 / 5 
    cheaper_price = min(apples_price, oranges_price)
    num_fruits = 12
    total_cost = cheaper_price * num_fruits
    result = total_cost
    return result

print(solution())