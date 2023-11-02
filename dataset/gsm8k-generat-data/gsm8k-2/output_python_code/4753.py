def solution():
    """Mickey's number is greater than Jayden's number by exactly 20. If Jayden's number is 40 less than Coraline's number, and Coraline's number is 80, calculate the total of the numbers they have."""
    coraline_num = 80
    jayden_num = coraline_num - 40
    mickey_num = jayden_num + 20
    total_num = coraline_num + jayden_num + mickey_num
    result = total_num
    return result

print(solution())