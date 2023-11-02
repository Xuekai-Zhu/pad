def solution():
     """A bulk warehouse is offering 48 cans of sparkling water for $12.00 a case. The local grocery store is offering the same sparkling water for $6.00 and it only has 12 cans. How much more expensive, per can, in cents, is this deal at the grocery store?"""
     cans_from_warehouse = 48
     price_from_warehouse = 1200
     grocery_store_cans = 12
     grocery_store_price = 600
     per_can_warehouse_price = price_from_warehouse / cans_from_warehouse
     per_can_grocery_store_price = grocery_store_price / grocery_store_cans
     grocery_store_markup = per_can_grocery_store_price - per_can_warehouse_price
     markup_in_cents = grocery_store_markup * 100
     result = markup_in_cents
     return result

print(solution())