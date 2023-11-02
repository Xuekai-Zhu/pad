def solution():
    """There are 200 more red apples than green apples in a grocery store. A truck arrives and delivers another 340 green apples. If there were originally 32 green apples, how many more green apples than red apples are there in the store now?"""
    initial_green_apples = 32
    initial_red_apples = initial_green_apples + 200
    green_apples_after_delivery = initial_green_apples + 340
    red_apples_after_delivery = initial_red_apples
    difference = green_apples_after_delivery - red_apples_after_delivery
    result = difference
    
    return result

print(solution())