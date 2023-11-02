def solution():
    # Calculate the percentage of boys at the school
    boys_percentage = 100 - 60
   
    # Calculate the total number of students at school
    total_students = (300 * 100) / boys_percentage
   
    # Calculate the number of girls at school
    girls = total_students - 300
    result = girls
    return result

print(solution())