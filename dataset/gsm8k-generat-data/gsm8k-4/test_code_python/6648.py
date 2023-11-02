def solution():
    """Donna bought 3 times as many pencils as Marcia did. Marcia bought double the number of pencils as Cindi did. How many pencils did Donna and Marcia buy altogether if Cindi spent $30 on $0.50 pencils?"""
    
    # Calculate the number of pencils Cindi bought
    cindi_pencils = 30 / 0.5

    # Calculate the number of pencils Marcia bought
    marcia_pencils = cindi_pencils * 2

    # Calculate the number of pencils Donna bought
    donna_pencils = marcia_pencils * 3

    # Calculate the total number of pencils bought by both Donna and Marcia
    total_pencils = donna_pencils + marcia_pencils

    # return the result
    result = total_pencils
    return result

print(solution())