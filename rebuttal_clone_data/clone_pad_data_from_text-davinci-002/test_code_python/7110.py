def solution():
     gallons_to_fill = 600
     gallons_per_bucket = 5
     buckets_per_trip = 2
     trips_per_hour = 3
 
     gallons_per_trip = gallons_per_bucket * buckets_per_trip
     hours_to_fill = gallons_to_fill / gallons_per_trip
     trips_to_fill = hours_to_fill * trips_per_hour
     result = trips_to_fill
     return result

print(solution())