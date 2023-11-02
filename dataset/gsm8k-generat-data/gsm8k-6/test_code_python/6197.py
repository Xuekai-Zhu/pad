def solution():
    # Find the value of the third number
    third_number = (500 - 200)/3  # since the sum of the three numbers is 500, and the first number is 200, the remaining sum is 300 which is divided equally among the second and third numbers.
    second_number = 2*third_number  # since the second number is twice the third number
    result = third_number
    return result

print(solution())