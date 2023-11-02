def solution():
     cost_per_box = 2
     cans_per_box = 10
    expected_consumption = 2
     number_of_attendees = 5 * 12
     number_of_boxes = number_of_attendees / expected_consumption
     total_cost = number_of_boxes * cost_per_box
     number_in_family = 6
     cost_per_person = total_cost / number_in_family
     result = cost_per_person
 
     return result

print(solution())