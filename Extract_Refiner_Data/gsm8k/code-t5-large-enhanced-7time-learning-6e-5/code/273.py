def solution():
    
    # Define the time it takes to dig a small hole and a large hole
    SMALL_HOUSE_TIME = 3
    LARGE_HOUSE_TIME = 10

    # Define the number of small and large holes to dig
    num_small_holes = 30
    num_large_holes = 15

    # Calculate the total time to dig all the holes
    total_time = (num_small_holes * SMALL_HOUSE_TIME) + (num_large_holes * LARGE_HOUSE_TIME)

    # Convert the total time to hours
    hours = total_time / 60

    # Display the hours it takes to dig all the holes
    result = hours
    return result

print(solution())