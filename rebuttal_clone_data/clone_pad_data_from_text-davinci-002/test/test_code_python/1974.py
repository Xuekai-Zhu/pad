def solution():
     bars_per_box = 3
     people = 6
     bars_needed = people * 2
     boxes_needed = bars_needed / bars_per_box
     cost_per_box = 7.50
     total_cost = boxes_needed * cost_per_box
     cost_per_person = total_cost / people
     result = cost_per_person
     return result

print(solution())