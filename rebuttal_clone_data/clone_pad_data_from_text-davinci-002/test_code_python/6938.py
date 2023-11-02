def solution():
 coal_cars = 6
 iron_cars = 12
 wood_cars = 2
 cars_deposited_at_each_station = 2 + 3 + 1
 miles_between_stations = 6
 minutes_between_stations = 25
 minutes_to_deliver_all_cars = coal_cars * minutes_between_stations + iron_cars * minutes_between_stations + wood_cars * minutes_between_stations
 result = minutes_to_deliver_all_cars
 return result

print(solution())