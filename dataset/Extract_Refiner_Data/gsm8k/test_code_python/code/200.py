def solution():
    
    # Define the initial number of green and yellow pens
    green_pens = 22
    yellow_pens = 10

    # Define the number of bags of blue and red pens purchased
    blue_bags = 6
    red_bags = 2

    # Calculate the total number of pens purchased
    total_purchased = (blue_bags * 9) + (red_bags * 6)

    # Calculate the total number of pens Janet has now
    total_pens = green_pens + yellow_pens + total_purchased

    # return the result
    result = total_pens
    return result

print(solution())