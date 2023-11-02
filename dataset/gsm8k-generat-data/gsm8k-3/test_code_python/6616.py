def solution():
    """In Grade 4, there are two sections -- Diligence and Industry. 
    The two sections have an equal number of students after 2 students were transferred from section Industry to Diligence. 
    How many students were there in section Diligence before the transfer if, in both sections combined, there are a total of 50 students?"""
    
    # Define the number of students in both sections combined
    total_students = 50
    
    # Define the number of students transferred from Industry to Diligence
    transfer_students = 2
    
    # Calculate the number of students in each section after the transfer
    equal_students = total_students / 2
    
    # Calculate the number of students in Diligence before the transfer
    diligence_students = equal_students + transfer_students
    
    # Display the number of students in Diligence before the transfer
    result = diligence_students
    return result

print(solution())