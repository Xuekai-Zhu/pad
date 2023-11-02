def solution():
     total_milk_tea = 50
     winter_melon_percent = 2/5
     winter_melon_cups = total_milk_tea * winter_melon_percent
     okinawa_percent = 3/10
     okinawa_cups = total_milk_tea * okinawa_percent
     chocolate_cups = total_milk_tea - winter_melon_cups - okinawa_cups
     result = chocolate_cups
 
     return result

print(solution())