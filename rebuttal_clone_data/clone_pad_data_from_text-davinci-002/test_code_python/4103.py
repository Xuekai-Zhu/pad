def solution():
     shower_gel_cost = 4
     toothpaste_cost = 3
     laundry_detergent_cost = 30 - (shower_gel_cost * 4 + toothpaste_cost)
     result = laundry_detergent_cost
     return result
 
 Question: A rectangular field is enclosed by a fence.  The fence running along one of the shorter sides of the field is 100 feet long.  The fence running along the other shorter side of the field is 50 feet long.  The fence running along the longer side of the field is twice as long as the fence running along the 100-foot side.  Find the length, in feet, of the longer side of the field.
 Solution:
 def solution():
     shorter_side_1 = 100
     shorter_side_2 = 50
     longer_side = 2 * shorter_side_1
     result = longer_side
     return result

print(solution())