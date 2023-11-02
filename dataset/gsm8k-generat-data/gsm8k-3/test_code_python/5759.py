def solution():
    """Jonathan's full name contains 8 letters for the first name and 10 letters for the surname. His sister's name has 5 letters for the first name and 10 letters for the second name. What's the total number of letters in their names?"""
    # Define the lengths of Jonathan's first and last names
    jon_first_name = 8
    jon_last_name = 10

    # Define the lengths of his sister's first and last names
    sis_first_name = 5
    sis_last_name = 10

    # Calculate the total number of letters in both names
    total_letters = jon_first_name + jon_last_name + sis_first_name + sis_last_name

    # Display the total number of letters
    result = total_letters
    return result

print(solution())