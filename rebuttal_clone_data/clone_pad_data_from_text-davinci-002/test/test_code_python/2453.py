def solution():
     individual_bookings = 12000
     group_bookings = 16000
     cancelled_bookings = 1600
     total_bookings = individual_bookings + group_bookings - cancelled_bookings
     result = total_bookings
     return result

print(solution())