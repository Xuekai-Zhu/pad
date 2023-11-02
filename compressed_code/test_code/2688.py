def solution():
   
   dinner_bill = (3/4) * 80
   money_left = (2 * 40) - dinner_bill - 2
   num_scoops = money_left // 3
   result = num_scoops
   return result

print(solution())