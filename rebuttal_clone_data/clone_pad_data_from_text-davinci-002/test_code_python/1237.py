def solution():
     suv_price = 7
     truck_price = 6
     car_price = 5
     total_price = 100
     suvs_washed = 5
     trucks_washed = 5
     total_cars_washed = (total_price - (suvs_washed * suv_price + trucks_washed * truck_price)) / car_price
     result = total_cars_washed
     return result

print(solution())