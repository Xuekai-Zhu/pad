def solution():
    # Define the initial number of roses planted
    roses_planted = 50

    # Calculate the number of roses planted on the second day
    day2_roses = roses_planted + 20

    # Calculate the number of roses planted on the third day
    day3_roses = 2 * roses_planted

    # Calculate the total number of roses planted
    total_roses = roses_planted + day2_roses + day3_roses
    result = total_roses
    return result

print(solution())