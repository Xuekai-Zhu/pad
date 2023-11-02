def solution():
    # Calculate the total number of donuts bought by Sophie
    total_donuts = 4 * 12  

    # Calculate the number of donuts given to Sophie's mom and sister
    given_donuts = 12 + 6  

    # Calculate the number of donuts left for Sophie
    left_donuts = total_donuts - given_donuts
    result = left_donuts
    return result

print(solution())