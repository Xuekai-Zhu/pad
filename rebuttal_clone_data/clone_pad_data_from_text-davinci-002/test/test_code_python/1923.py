def solution():
     bag_of_flour = 500
     flour_used = 240
     flour_spilled = (bag_of_flour - flour_used) / 2
     flour_needed = bag_of_flour - flour_spilled
     result = flour_needed
     return result

print(solution())