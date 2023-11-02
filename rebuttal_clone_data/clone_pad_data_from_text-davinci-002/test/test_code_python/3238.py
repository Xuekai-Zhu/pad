def solution():
     cost_of_milk_tea = 2.40
     cost_of_one_slice_of_cake = cost_of_milk_tea * 3 / 4
     cost_of_two_slices_of_cake = cost_of_one_slice_of_cake * 2
     cost_of_one_cup_of_milk_tea = cost_of_milk_tea
     total_cost = cost_of_two_slices_of_cake + cost_of_one_cup_of_milk_tea
     result = total_cost
     return result

print(solution())