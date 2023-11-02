def solution():
    """Grant has worked as a freelance math worker for the last three months.  The first month he made 350$.  The second month he made 50$ more than double he made the first month.  The third month he quadrupled the sum of the first two months.  How much did Grant make in his first three months total?"""
    # Define the amount made in the first month
    month1 = 350

    # Define the amount made in the second month
    month2 = (2 * month1) + 50

    # Define the amount made in the third month
    month3 = 4 * (month1 + month2)

    # Calculate the total amount made in the first three months
    total = month1 + month2 + month3

    # return the result
    result = total
    return result

print(solution())