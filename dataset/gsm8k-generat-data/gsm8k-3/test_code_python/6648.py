def solution():
    """Donna bought 3 times as many pencils as Marcia did. 
    Marcia bought double the number of pencils as Cindi did. 
    How many pencils did Donna and Marcia buy altogether if Cindi spent $30 on $0.50 pencils?"""
    # Define the cost per pencil
    COST_PER_PENCIL = 0.5

    # Calculate the number of pencils Cindi bought
    cindi_pencils = 30 / COST_PER_PENCIL

    # Calculate the number of pencils Marcia bought
    marcia_pencils = 2 * cindi_pencils

    # Calculate the number of pencils Donna bought
    donna_pencils = 3 * marcia_pencils

    # Calculate the total number of pencils bought by Donna and Marcia
    total_pencils = marcia_pencils + donna_pencils

    # Display the total number of pencils
    result = total_pencils
    return result

print(solution())