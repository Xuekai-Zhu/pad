def solution():
    """Sally took 342 pens to her class of 44 students. If she gave 7 pens to each student, left half of the remainder in her locker, and took the rest home, how many did she take home?"""
    # Calculate the total number of pens given to students
    pens_given = 7 * 44

    # Calculate the remainder of pens
    remainder = 342 - pens_given

    # Calculate the number of pens Sally left in her locker
    pens_locker = remainder // 2

    # Calculate the number of pens Sally took home
    pens_home = remainder - pens_locker

    # Display the number of pens Sally took home
    result = pens_home
    return result

print(solution())