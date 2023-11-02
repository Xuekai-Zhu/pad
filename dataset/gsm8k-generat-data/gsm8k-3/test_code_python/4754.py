def solution():
    """Mickey's number is greater than Jayden's number by exactly 20. If Jayden's number is 40 less than Coraline's number, and Coraline's number is 80, calculate the total of the numbers they have."""
    # Define Coraline's number
    coraline_num = 80

    # Calculate Jayden's number
    jayden_num = coraline_num - 40

    # Calculate Mickey's number
    mickey_num = jayden_num + 20

    # Calculate the total of their numbers
    total = coraline_num + jayden_num + mickey_num

    # Display the total
    result = total
    return result

print(solution())