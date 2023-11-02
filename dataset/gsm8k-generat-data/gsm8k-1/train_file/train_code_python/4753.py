def solution():
    """Mickey's number is greater than Jayden's number by exactly 20. If Jayden's number is 40 less than Coraline's number, and Coraline's number is 80, calculate the total of the numbers they have."""
    coraline = 80
    jayden = coraline - 40
    mickey = jayden + 20
    total = coraline + jayden + mickey
    result = total
    return result

print(solution())