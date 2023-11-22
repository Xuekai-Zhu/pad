def solution():
    
    # Define the number of stripes per zebra and zebras
    stripes_per_zebra = 36 / 2
    stripes_per_zebras = 17 + 36

    # Calculate the total number of stripes
    total_stripes = stripes_per_zebra * 2 + stripes_per_zebras

    # Calculate the average number of stripes
    avg_stripes = total_stripes / 2

    # Display the average number of stripes
    result = avg_stripes
    return result

print(solution())