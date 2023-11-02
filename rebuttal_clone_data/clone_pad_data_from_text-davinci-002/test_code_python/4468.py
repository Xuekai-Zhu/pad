def solution():
     cost_per_box = 9
     boxes_bought = 12
     masks_per_box = 50
     boxes_repacked = 6
     cost_per_repacked_box = cost_per_box / 2
     masks_sold_bagged = 300
     bagged_price = 3
     profit = (cost_per_repacked_box * boxes_repacked) + (masks_sold_bagged * (bagged_price - 1))
     result = profit
     return result

print(solution())