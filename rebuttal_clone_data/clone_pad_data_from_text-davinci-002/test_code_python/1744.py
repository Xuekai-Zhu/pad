def solution():
     potatoes_harvested = 250
     carrots_harvested = 320
     potatoes_bundled = 25
     carrots_bundled = 20
     potato_bundle_price = 1.90
     carrot_bundle_price = 2
 
     total_potatoes_sold = potatoes_harvested / potatoes_bundled
     total_carrots_sold = carrots_harvested / carrots_bundled
 
     total_revenue = total_potatoes_sold * potato_bundle_price + total_carrots_sold * carrot_bundle_price
     result = total_revenue
     return result

print(solution())