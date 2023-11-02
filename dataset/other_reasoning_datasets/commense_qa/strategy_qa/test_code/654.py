def solution():
    # Define the length of an average ruler and the length range of a giant armadillo
    average_ruler_length = 30 # in centimeters
    giant_armadillo_length_range = range(75, 101) # in centimeters, including both endpoints
    # Calculate the total length of a giant armadillo with its tail
    giant_armadillo_total_length = max(giant_armadillo_length_range) + 50 # in centimeters
    # Check if multiple rulers would be needed to measure the giant armadillo's length
    if giant_armadillo_total_length > average_ruler_length:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())