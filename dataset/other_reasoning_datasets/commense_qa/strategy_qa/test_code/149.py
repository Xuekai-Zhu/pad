def solution():
    # Define the average length of a beaver's teeth in millimeters and the length of a Smilodon's teeth in inches
    beaver_teeth_length = 25
    smilodon_teeth_length = 11 * 25.4 # Convert inches to millimeters
    # Check if the length of the beaver's teeth is greater than or equal to the length of the Smilodon's teeth
    if beaver_teeth_length >= smilodon_teeth_length:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())