def solution():
     family_height = 80
     neighbor_one_height = 70
     neighbor_two_height = 99
     total_height = family_height + neighbor_one_height + neighbor_two_height
     average_height = total_height / 3
     difference = average_height - family_height
     result = difference
     return result

print(solution())