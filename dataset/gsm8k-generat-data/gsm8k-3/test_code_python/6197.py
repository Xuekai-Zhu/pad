def solution():
    """The sum of the three numbers is 500. If the first number is 200, and the value of the second number is twice the value of the third number, find the value of the third number."""
    # Define the first number and sum of all three numbers
    first_number = 200
    total_sum = 500

    # Calculate the sum of the second and third number
    second_third_sum = total_sum - first_number

    # Define the relationship between the second and third number
    second_third_ratio = 2

    # Calculate the value of the third number
    third_number = second_third_sum / (second_third_ratio + 1)

    result = third_number
    return result

print(solution())