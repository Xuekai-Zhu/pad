def solution():
    """The sum of the three numbers is 500. If the first number is 200, and the value of the second number is twice the value of the third number, find the value of the third number."""
    first_num = 200
    sum_of_three = 500
    second_num = 2 * third_num
    third_num = (sum_of_three - first_num - second_num) / 3
    result = third_num
    return result

print(solution())