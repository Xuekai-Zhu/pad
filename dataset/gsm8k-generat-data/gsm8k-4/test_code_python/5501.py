def solution():
    """There are 200 more red apples than green apples in a grocery store. A truck arrives and delivers another 340 green apples. If there were originally 32 green apples, how many more green apples than red apples are there in the store now?"""
    # Define the initial number of green apples
    green_apples = 32

    # Calculate the number of red apples
    red_apples = green_apples + 200

    # Add the 340 green apples delivered by the truck
    green_apples += 340

    # Calculate the difference between the number of green and red apples
    diff = green_apples - red_apples

    # return the result
    result = diff
    return result

print(solution())