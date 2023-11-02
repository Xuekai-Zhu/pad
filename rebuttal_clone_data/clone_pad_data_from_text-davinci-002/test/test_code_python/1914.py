def solution():
   crab_baskets_per_week = 3
   crabs_per_basket = 4
   collections_per_week = 2
   price_per_crab = 3
   total_crabs = crab_baskets_per_week * crabs_per_basket
   crabs_collected = collections_per_week * total_crabs
   money_made = crabs_collected * price_per_crab
   result = money_made
   return result

print(solution())