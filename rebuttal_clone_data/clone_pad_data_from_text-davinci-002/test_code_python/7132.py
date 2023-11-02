def solution():
     baking_trays = 4
     cupcakes_per_tray = 20
     cupcakes_sold = (3/5) * (baking_trays * cupcakes_per_tray)
     cupcakes_kept = baking_trays * cupcakes_per_tray - cupcakes_sold
     price_per_cupcake = 2
     money_made = cupcakes_sold * price_per_cupcake
     result = money_made
     return result

print(solution())