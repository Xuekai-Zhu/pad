def solution():
     flour = 2
     sugar = 1
     eggs_and_butter = 1.5
     blueberries = 3
     cherry = 4
     
     blueberries_in_oz = 3 * 8
     blueberry_price = 2.25 * blueberries_in_oz
     cherry_in_oz = 4 * 16
     cherry_price = 4 / cherry_in_oz
     
     total_price_blueberry = flour + sugar + eggs_and_butter + blueberry_price
     total_price_cherry = flour + sugar + eggs_and_butter + cherry_price
     
     if total_price_blueberry < total_price_cherry:
         result = "The cheapest pie is blueberry and it costs " + str(total_price_blueberry)
     else: 
         result = "The cheapest pie is cherry and it costs " + str(total_price_cherry)
     return result

print(solution())