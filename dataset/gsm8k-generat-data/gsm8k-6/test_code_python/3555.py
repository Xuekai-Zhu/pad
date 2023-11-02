def solution():
    # Calculate the number of pens Alex has after a month
    alex_pens = 4 * (2 ** 4) # Alex's pen collection doubles every week, so after 4 weeks it will be 4 * 2^4 

    # Calculate the difference between Alex's and Jane's pen collections
    jane_pens = 16
    difference = alex_pens - jane_pens
    result = difference
    return result

print(solution())