def solution():
    """Andy gets a cavity for every 4 candy canes he eats. He gets 2 candy canes from his parents and 3 candy canes each from 4 teachers. Then he uses his allowance to buy 1/7 as many candy canes as he was given. How many cavities does he get from eating all his candy canes?"""
    # Define the number of candy canes Andy gets
    parent_candy_canes = 2
    teacher_candy_canes = 3 * 4
    total_candy_canes = parent_candy_canes + teacher_candy_canes

    # Calculate the number of candy canes he buys with his allowance
    allowance_candy_canes = total_candy_canes * (1/7)

    # Calculate the total number of candy canes he has
    total_candy_canes += allowance_candy_canes

    # Calculate the number of cavities he gets
    cavities = total_candy_canes // 4

    # Display the number of cavities
    result = cavities
    return result

print(solution())