def solution():
    # Calculate the number of pens given to the students
    pens_given = 7 * 44  

    # Calculate the remaining pens after giving to the students
    pens_remaining = 342 - pens_given  

    # Calculate the number of pens Sally left in her locker
    pens_left = pens_remaining // 2  

    # Calculate the number of pens Sally took home
    pens_taken_home = pens_remaining - pens_left  

    result = pens_taken_home
    return result

print(solution())