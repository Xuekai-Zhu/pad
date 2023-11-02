def solution():
     starting_gallons = 40
     loss_per_hour = 2
     first_two_hours = 2
     third_hour = 1
     fourth_hour = 3
 
     total_loss = (loss_per_hour * first_two_hours) + third_hour + fourth_hour
 
     gallons_remaining = starting_gallons - total_loss
 
     result = gallons_remaining
 
     return result

print(solution())