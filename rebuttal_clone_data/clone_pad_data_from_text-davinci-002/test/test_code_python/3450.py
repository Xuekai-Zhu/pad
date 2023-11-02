def solution():
     original_amount = 30
     amount_burned = original_amount / 2
     amount_eaten = original_amount - amount_burned
     percent_eaten = 80
     actual_amount_eaten = amount_eaten * (percent_eaten / 100)
     result = actual_amount_eaten
 
     return result

print(solution())