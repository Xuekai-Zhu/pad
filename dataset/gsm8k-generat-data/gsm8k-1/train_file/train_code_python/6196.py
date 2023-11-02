def solution():
    """The sum of the three numbers is 500. If the first number is 200, and the value of the second number is twice the value of the third number, find the value of the third number."""
    first_number = 200
    total_sum = 500
    second_number = total_sum - first_number
    third_number = second_number / 3
    result = third_number
    return result

print(solution())