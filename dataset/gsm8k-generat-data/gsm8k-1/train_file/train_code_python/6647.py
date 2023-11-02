def solution():
    """Donna bought 3 times as many pencils as Marcia did. Marcia bought double the number of pencils as Cindi did.
    How many pencils did Donna and Marcia buy altogether if Cindi spent $30 on $0.50 pencils?"""
    cindi_spent = 30
    pencil_price = 0.5
    cindi_pencils = cindi_spent / pencil_price
    marcia_pencils = cindi_pencils * 2
    donna_pencils = marcia_pencils * 3
    total_pencils = cindi_pencils + marcia_pencils + donna_pencils
    result = total_pencils
    return result

print(solution())