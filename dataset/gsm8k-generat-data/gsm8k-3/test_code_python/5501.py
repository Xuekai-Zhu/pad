def solution():
    """There are 200 more red apples than green apples in a grocery store. A truck arrives and delivers another 340 green apples. If there were originally 32 green apples, how many more green apples than red apples are there in the store now?"""
    # Define the number of green apples originally in the store
    green_apples_orig = 32

    # Calculate the number of red apples originally in the store
    red_apples_orig = green_apples_orig + 200

    # Calculate the total number of apples originally in the store
    total_apples_orig = green_apples_orig + red_apples_orig

    # Calculate the additional green apples delivered by the truck
    additional_green_apples = 340

    # Calculate the new total number of green apples
    total_green_apples = green_apples_orig + additional_green_apples

    # Calculate the new total number of red apples
    total_red_apples = total_apples_orig - total_green_apples

    # Calculate the difference between the new total number of green apples and the new total number of red apples
    difference = total_green_apples - total_red_apples

    # Display the difference between the new total number of green apples and the new total number of red apples
    result = difference
    return result

print(solution())