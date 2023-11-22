def solution():
    
    # Define the total number of burritos ordered
    total_burritos = 600

    # Define the number of students and the number of burritos per student
    num_students = 50
    burritos_per_student = 10

    # Calculate the total number of burritos given to students
    total_given_burritos = num_students * burritos_per_student

    # Calculate the number of burritos eaten by Mr. George
    burritos_eaten = 20

    # Calculate the number of leftover burritos
    leftover_burritos = total_burritos - total_given_burritos - burritos_eaten

    # Display the number of leftover burritos
    result = leftover_burritos
    return result

print(solution())