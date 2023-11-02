def solution():
     jeans_price = 11
     tees_price = 8
     jeans_sold = 4
     tees_sold = 7
     total_sold = jeans_sold + tees_sold
     total_price = jeans_price * jeans_sold + tees_price * tees_sold
     result = total_price
     return result

print(solution())