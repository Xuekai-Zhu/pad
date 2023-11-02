def solution():
     total_bracelets = 52
     bracelets_given_away = 8
     bracelets_sold = total_bracelets - bracelets_given_away
     sale_price_per_bracelet = 0.25
     cost_per_bracelet = 3.00
     total_sale_price = bracelets_sold * sale_price_per_bracelet
     total_cost = total_bracelets * cost_per_bracelet
     profit = total_sale_price - total_cost
     result = profit
     return result

print(solution())