def solution():
    
    shirts_sold = 20
    jeans_sold = 10
    shirt_price = 10
    jeans_price = 2 * shirt_price
    total_earned = (shirts_sold * shirt_price) + (jeans_sold * jeans_price)
    result = total_earned
    return result

print(solution())