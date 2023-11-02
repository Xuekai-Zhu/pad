def solution():
     total_homes = 200
     homes_delivered_first_hour = int(total_homes * 2/5)
     homes_delivered_second_hour = int(total_homes * 3/5)
     homes_delivered_third_hour = int(total_homes * 4/5)
   
     total_homes_delivered = homes_delivered_first_hour + homes_delivered_second_hour + homes_delivered_third_hour
     homes_remaining = total_homes - total_homes_delivered
     result = homes_remaining
 
     return result

print(solution())