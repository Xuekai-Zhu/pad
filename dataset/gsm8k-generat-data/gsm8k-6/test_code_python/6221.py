def solution():
    # Calculate the number of students from Karen High School
    Karen_students = (3/5) * 50
  
    # Calculate the combined number of students from Know It All and Karen High Schools
    KIA_Karen_students = 50 + Karen_students
    
    # Calculate the number of students from Novel Corona High School
    NC_students = 2 * KIA_Karen_students
    
    # Calculate the total number of students at the competition
    total_students = KIA_Karen_students + NC_students
    result = total_students
    return result

print(solution())