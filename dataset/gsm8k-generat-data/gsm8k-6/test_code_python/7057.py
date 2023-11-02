def solution():
    # Calculate the number of red flowers
    red_flowers = 3 * 9  # three times more red flowers than green flowers
 
    # Calculate the number of blue flowers
    blue_flowers = 0.5 * 96  # blue flowers make up 50% of the total flower count
 
    # Calculate the number of yellow flowers
    yellow_flowers = 96 - (9 + red_flowers + blue_flowers)
 
    result = yellow_flowers
    return result

print(solution())