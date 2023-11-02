def solution():
    """Donna bought 3 times as many pencils as Marcia did. Marcia bought double the number of pencils as Cindi did. How many pencils did Donna and Marcia buy altogether if Cindi spent $30 on $0.50 pencils?"""
    cindi_pencils = 30/0.5
    marcia_pencils = 2 * cindi_pencils
    donna_pencils = 3 * marcia_pencils
    total_pencils = marcia_pencils + donna_pencils
    result = total_pencils
    return result

print(solution())