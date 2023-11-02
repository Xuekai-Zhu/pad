def solution():
     desired_flour = 6
     capacity_of_scoop = 1/4
     total_capacity = 8
     scoops_to_remove = (total_capacity - desired_flour) / capacity_of_scoop
     result = scoops_to_remove
     return result

print(solution())