def solution():
     total_students = 12 + 10
     fraction_girls_reading = 5/6
     fraction_boys_reading = 4/5
     total_students_reading = fraction_girls_reading * 12 + fraction_boys_reading * 10
     total_students_not_reading = total_students - total_students_reading
     result = total_students_not_reading
 
     return result

print(solution())