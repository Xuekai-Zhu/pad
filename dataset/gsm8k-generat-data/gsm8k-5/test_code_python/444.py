def solution():
    reggie_score = (3*1) + (2*2) + (1*3)  # Reggie's score is three 1-pointers, two 2-pointers, and one 3-pointer
    brother_score = 4 * 3  # Reggie's brother made 4 long shots, each worth 3 points

    # Calculate the difference in points between Reggie and his brother
    difference = brother_score - reggie_score
    result = difference
    return result

print(solution())