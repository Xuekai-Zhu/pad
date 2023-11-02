def solution():
     water_jug_capacity = 40
     students = 200
     cups_of_water_per_student = 10
     water_jugs_needed = (students * cups_of_water_per_student) / water_jug_capacity
     result = water_jugs_needed
 
     return result

print(solution())