def solution():
     cost_per_box = 10
     pens_per_box = 30
     pens_per_package = 6
     boxes_per_package = 5
     sale_price_per_package = 3
     cost_per_package = cost_per_box * boxes_per_package
     pens_leftover = pens_per_box - (pens_per_package * boxes_per_package)
     cost_per_highlighter = cost_per_box / pens_per_box
     sale_price_per_highlighter = 2 / 3
     profit_per_package = sale_price_per_package - cost_per_package
     profit_per_highlighter = sale_price_per_highlighter - cost_per_highlighter
     total_profit = (profit_per_package * boxes_per_package) + (profit_per_highlighter * pens_leftover)
     result = total_profit
     return result

print(solution())