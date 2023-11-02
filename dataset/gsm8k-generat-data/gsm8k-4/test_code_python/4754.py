def solution():
    """Mickey's number is greater than Jayden's number by exactly 20. If Jayden's number is 40 less than Coraline's number, and Coraline's number is 80, calculate the total of the numbers they have."""
    # Calculate Jayden's number
    jayden_number = 80 - 40

    # Calculate Mickey's number
    mickey_number = jayden_number + 20

    # Calculate the total of the numbers they have
    total = jayden_number + mickey_number + 80

    # return the result
    result = total
    return result

print(solution())