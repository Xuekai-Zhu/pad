def solution():
    """The sum of the three numbers is 500. If the first number is 200, and the value of the second number is twice the value of the third number, find the value of the third number."""
    # Define the known values
    total = 500
    first = 200
    second = None
    third = None

    # Calculate the sum of the second and third numbers
    # The sum of all three numbers is total - first
    second_and_third = total - first

    # Divide the sum of the second and third numbers by 3 to get the average value
    avg_value = second_and_third / 3

    # Since the second number is twice the third number, we can set up the equation:
    # second = 2*third
    # We can substitute second with 2*third and solve for third
    # first + second + third = total
    # 200 + 2*third + third = 500
    # 3*third = 300
    # third = 100
    third = 100

    # Double the value of the third number to get the value of the second number
    second = 2 * third

    result = third
    return result

print(solution())