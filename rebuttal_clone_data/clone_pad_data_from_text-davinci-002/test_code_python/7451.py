def solution():
     cost_to_make_cars = 100
     number_of_cars = 4
     sales_price_cars = 50
     cost_to_make_motorcycles = 250
     number_of_motorcycles = 8
     sales_price_motorcycles = 50
     profit_cars = sales_price_cars * number_of_cars - cost_to_make_cars
     profit_motorcycles = sales_price_motorcycles * number_of_motorcycles - cost_to_make_motorcycles
     difference_in_profit = profit_motorcycles - profit_cars
     result = profit_motorcycles
     return result

print(solution())