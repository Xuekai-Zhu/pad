def solution():
    """Brad’s zip code consists of five numbers that add up to 10. The first and second numbers are the same. The third number is zero. The fourth number is double the first number. The fourth and fifth numbers add up to 8. What is Brad’s zip code?"""
    # Define the variables
    first_num = None
    second_num = None
    third_num = 0
    fourth_num = None
    fifth_num = None

    # Set up the equations to solve for the variables
    # first_num + second_num + third_num + fourth_num + fifth_num = 10
    # first_num = second_num
    # fourth_num = 2 * first_num
    # fourth_num + fifth_num = 8

    # Substitute and simplify
    # 2 * first_num + third_num + 3 * fourth_num = 18
    # 2 * first_num + 2 * fourth_num = 8

    # Solve for first_num and fourth_num
    first_num = 2
    fourth_num = 3

    # Solve for second_num and fifth_num
    second_num = 2
    fifth_num = 5

    # Concatenate the numbers to form Brad's zip code
    brads_zipcode = f"{first_num}{second_num}{third_num}{fourth_num}{fifth_num}"

    # return the result
    result = brads_zipcode
    return result

print(solution())