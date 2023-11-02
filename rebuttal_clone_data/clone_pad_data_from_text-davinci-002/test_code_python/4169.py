def solution():
     apples = 180
     plums = apples / 3
     total_fruits = apples + plums
     picked_fruits = 3/5 * total_fruits
     remaining_fruits = total_fruits - picked_fruits
     apples_remaining = remaining_fruits / 2
     plums_remaining = remaining_fruits / 4
     result = (apples_remaining, plums_remaining)
 
    return result

print(solution())