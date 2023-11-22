def solution():
    
    # Define the number of adults and babies
    adults = 42
    babies = 15

    # Calculate the total number of chairs
    total_chairs = adults + babies

    # Calculate the number of regular chairs
    regular_chairs = 5 * 8

    # Calculate the total number of chairs
    total_chairs += regular_chairs

    # Calculate the number of chairs left to get
    chairs_left = total_chairs - 8

    # Display the number of chairs left to get
    result = chairs_left
    return result

print(solution())