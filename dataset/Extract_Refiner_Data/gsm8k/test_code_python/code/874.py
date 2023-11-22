def solution():
    
    # Define the total number of glasses sold
    total_glasses_sold = 32

    # Calculate the number of glasses sold by Julie and Micah
    julie_glasses_sold = 14
    micah_glasses_sold = (total_glasses_sold - julie_glasses_sold) / 2

    # Calculate the difference between the number of glasses sold by Julie and Micah
    difference = julie_glasses_sold - micah_glasses_sold

    # return the result
    result = difference
    return result

print(solution())