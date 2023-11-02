def solution():
     glasses_per_gallon = 16
     cost_per_gallon = 3.50
     number_of_gallons = 2
     price_per_glass = 1.00
     glasses_consumed = 5
     glasses_sold = glasses_per_gallon * number_of_gallons - glasses_consumed - 6
     total_revenue = glasses_sold * price_per_glass
     total_cost = cost_per_gallon * number_of_gallons
     net_profit = total_revenue - total_cost
 
     return net_profit

print(solution())