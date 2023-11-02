def solution():
     miles = 600
     hours = miles / 50
     minutes = hours * 60
     rest_stops = minutes / 120
     minutes_for_rest_stops = rest_stops * 15
     gallons = miles / 18
     minutes_to_refill = gallons / 15 * 10
     total_minutes = minutes + minutes_for_rest_stops + minutes_to_refill
     result = total_minutes
     return result

print(solution())