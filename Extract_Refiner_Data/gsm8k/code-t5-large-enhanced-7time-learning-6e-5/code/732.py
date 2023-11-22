def solution():
    
    # Define the initial number of apples Boris has
    boris_apples = 100

    # Calculate the number of apples Beck has
    beck_apples = boris_apples - 23

    # Subtract 10 apples Boris gives Beck
    boris_apples -= 10

    # Calculate the difference between Beck's and Boris's number of apples
    difference = beck_apples - boris_apples

    # Display the difference
    result = difference
    return result

print(solution())