def solution():
    """There are 200 more red apples than green apples in a grocery store. A truck arrives and delivers another 340 green apples. If there were originally 32 green apples, how many more green apples than red apples are there in the store now?"""
    original_green_apples = 32
    original_red_apples = original_green_apples + 200
    new_green_apples = original_green_apples + 340
    new_red_apples = original_red_apples
    difference = new_green_apples - new_red_apples
    result = difference
    return result

print(solution())