def solution():
    """Andy gets a cavity for every 4 candy canes he eats. He gets 2 candy canes from his parents and 3 candy canes each from 4 teachers. Then he uses his allowance to buy 1/7 as many candy canes as he was given. How many cavities does he get from eating all his candy canes?"""
    # Define the number of candy canes received from different sources
    parent_candy = 2
    teacher_candy = 3
    total_teacher_candy = teacher_candy * 4
    allowance_candy = total_teacher_candy / 7

    # Calculate the total number of candy canes
    total_candy = parent_candy + total_teacher_candy + allowance_candy

    # Calculate the total number of cavities
    total_cavities = total_candy // 4

    # return the result
    result = total_cavities
    return result

print(solution())