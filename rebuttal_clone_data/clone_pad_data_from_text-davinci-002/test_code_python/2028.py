def solution():
     initial_stock = 200
     remaining_stock = initial_stock / 2
     total_stock = initial_stock + remaining_stock
     rings_sold = total_stock * 3/4
     rings_bought = 300
     rings_sold_2 = rings_bought / 2
     final_stock = total_stock - rings_sold - rings_sold_2
     result = final_stock
     return result

print(solution())