def solution():
     shirts_sold = 20
     jeans_sold = 10
     shirt_price = 10
     jeans_price = shirt_price * 2
     total_sales = shirts_sold * shirt_price + jeans_sold * jeans_price
     result = total_sales
     return result

print(solution())