def solution():
     regular_duck_price = 3
     large_duck_price = 5
     regular_ducks_sold = 221
     large_ducks_sold = 185
     total_ducks_sold = regular_ducks_sold + large_ducks_sold
     total_revenue = regular_duck_price * regular_ducks_sold + large_duck_price * large_ducks_sold
 
     return total_revenue

print(solution())