def solution():
    # Calculate the number of kids that came to the 2005 cookout
    num_kids_2006 = 20
    num_kids_2005 = num_kids_2006 / (2/3)  # 2/3 as many kids came to the cookout in 2006 as in 2005

    # Calculate the number of kids that came to the 2004 cookout
    num_kids_2004 = num_kids_2005 * 2

    result = num_kids_2004
    return result

print(solution())