def solution():
    """Sara and Joe have a combined height of 120 inches. Joe is 6 inches more than double Sara's height. How tall is Joe?"""
    sara_height = (120 - 6) / 3      # divide by 3 since Joe is 2 times Sara + 6 and they have a combined height of 120
    joe_height = 2 * sara_height + 6
    result = joe_height
    return result

print(solution())