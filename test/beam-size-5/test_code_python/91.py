def solution():
    
    # Define the total number of students and the fraction that are boys
    total_students = 200
    boys_fraction = 2/5

    # Calculate the number of boys and girls
    boys = total_students * boys_fraction
    girls = total_students - boys

    # Calculate the number of girls in the girl scout
    girls_in_girl_scout = girls * (2/3)

    # Calculate the number of girls not in the girl scout
    girls_not_in_girl_scout = girls - girls_in_girl_scout

    # Display the number of girls not in the girl scout
    result = girls_not_in_girl_scout
    return result

print(solution())