def solution():
     initial_inventory = 4500
     bottles_sold_Monday = 2445
     bottles_sold_Tuesday = 900
     bottles_sold_Wednesday = 50
     bottles_sold_Thursday = 50
     bottles_sold_Friday = 50
     bottles_sold_Saturday = 50
     bottles_sold_Sunday = 50
     bottles_delivered_Saturday = 650
     
     bottles_left = initial_inventory - bottles_sold_Monday - bottles_sold_Tuesday - bottles_sold_Wednesday - bottles_sold_Thursday - bottles_sold_Friday

print(solution())