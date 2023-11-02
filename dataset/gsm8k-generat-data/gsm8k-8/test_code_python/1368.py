def solution():
    # Define Tamara's height as 3 times Kim's height minus 4 inches
    tamara_height = 3 * kim_height - 4

    # Define the equation for their combined height
    combined_height = tamara_height + kim_height

    # Solve for Kim's height using the combined height equation
    kim_height = (combined_height - tamara_height) / 2

    # Solve for Tamara's height using the equation above
    tamara_height = 3 * kim_height - 4

    result = tamara_height
    return result

print(solution())