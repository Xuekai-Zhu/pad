def solution():
    
    apple_price = 2/10  
    orange_price = 1.5/5  
    cheaper_fruit_price = min(apple_price, orange_price)
    cheaper_fruit_cost = cheaper_fruit_price * 12
    result = int(cheaper_fruit_cost * 100)  
    return result

print(solution())