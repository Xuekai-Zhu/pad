def solution():
    
    # Define the total number of students and the percentage of girls
    total_students = 80
    girls_percentage = 40

    # Calculate the number of girls in each class
    girls_per_class = total_students * (girls_percentage / 100)

    # Calculate the number of boys in each class
    boys_per_class = total_students - girls_per_class

    # Display the number of boys in each class
    result = boys_per_class
    return result

print(solution())