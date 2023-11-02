def solution():
     Caleb_bucket = 7
     Cynthia_bucket = 8
     total_gallons = 105
     number_of_trips = total_gallons / (Caleb_bucket + Cynthia_bucket)
     result = number_of_trips
     return result

print(solution())