def solution():
    # Calculate the sales on the first day
    tulip1 = 30
    rose1 = 20

    # Calculate the sales on the second day
    tulip2 = tulip1 * 2
    rose2 = rose1 * 2

    # Calculate the sales on the third day
    tulip3 = tulip2 * 0.1
    rose3 = 16

    # Calculate the total earnings
    earnings = (tulip1 * 2) + (rose1 * 3) + (tulip2 * 2) + (rose2 * 3) + (tulip3 * 2) + (rose3 * 3)

    result = earnings
    return result

print(solution())