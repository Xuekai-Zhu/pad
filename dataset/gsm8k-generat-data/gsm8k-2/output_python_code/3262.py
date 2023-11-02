def solution():
    """Andy gets a cavity for every 4 candy canes he eats. He gets 2 candy canes from his parents and 3 candy canes each from 4 teachers. Then he uses his allowance to buy 1/7 as many candy canes as he was given. How many cavities does he get from eating all his candy canes?"""
    candy_from_parents = 2
    candy_from_teachers = 3 * 4
    total_candy = candy_from_parents + candy_from_teachers
    candy_from_allowance = total_candy / 7
    total_candy += candy_from_allowance
    cavities = total_candy // 4
    result = cavities
    return result

print(solution())