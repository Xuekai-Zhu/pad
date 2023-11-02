def solution():
    
    # Define the number of stripes on each zebra
    zebra1_stripes = 17
    zebra2_stripes = 36
    zebra3_stripes = zebra1_stripes / 2

    # Calculate the total number of stripes
    total_stripes = zebra1_stripes + zebra2_stripes + zebra3_stripes

    # Calculate the average number of stripes
    average_stripes = total_stripes / 2

    # Display the average number of stripes
    result = average_stripes
    return result

print(solution())