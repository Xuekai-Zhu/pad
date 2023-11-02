def solution():
     time_to_hidden_lake = 15
     time_from_hidden_lake_to_park_office = 7
     time_gone_altogether = time_to_hidden_lake + time_from_hidden_lake_to_park_office
     time_to_restaurant = time_gone_altogether - time_to_hidden_lake
     result = time_to_restaurant
     return result

print(solution())