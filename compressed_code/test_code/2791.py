def solution():
    
    mangoes = 400
    apples = 2 * mangoes
    oranges = mangoes + 200
    total_produce = mangoes + apples + oranges
    fruit_price = 50
    total_money = total_produce * fruit_price
    result = total_money
    return result

print(solution())