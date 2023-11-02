def solution():
     hawk_feathers = 6
     eagle_feathers = hawk_feathers * 17
     total_feathers = hawk_feathers + eagle_feathers
     given_away = 10
     remaining_feathers = total_feathers - given_away
     feathers_sold = remaining_feathers / 2
     feathers_left = remaining_feathers - feathers_sold
     result = feathers_left
 
     return result

print(solution())