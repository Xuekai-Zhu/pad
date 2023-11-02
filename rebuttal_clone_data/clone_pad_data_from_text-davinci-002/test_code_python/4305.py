def solution():
     eggs_sold_Monday = 5
     eggs_sold_Tuesday = 2 * eggs_sold_Monday
     eggs_sold_Wednesday = eggs_sold_Tuesday - 2
     eggs_sold_Thursday = eggs_sold_Tuesday / 2
     total_eggs_sold = eggs_sold_Monday + eggs_sold_Tuesday + eggs_sold_Wednesday + eggs_sold_Thursday
     result = total_eggs_sold
     return result

print(solution())