def solution():
    # Define the variables for Palm Beach's area and average palm length
    palm_beach_area = 8.12
    average_palm_length_in_inches = 3
    inches_in_a_square_mile = 63360 ** 2
    
    # Calculate the total area of Palm Beach in square inches
    palm_beach_area_in_inches = palm_beach_area * inches_in_a_square_mile
    
    # Check if Palm Beach can be held in the palm of your hand
    if palm_beach_area_in_inches <= average_palm_length_in_inches ** 2:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())