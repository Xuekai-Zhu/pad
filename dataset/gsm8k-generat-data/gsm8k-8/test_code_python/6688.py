def solution():
  # Calculate the number of computers needed with 82 students
  num_computers_82_students = 82/2
  
  # Calculate the number of students without enough computers
  num_students_without_computers = 82 + 16 - num_computers_82_students*2
  
  # Calculate the total number of computers needed with the additional 16 students
  total_num_computers = (82+16)/2 + num_students_without_computers/2
  
  result = total_num_computers
  return result

print(solution())