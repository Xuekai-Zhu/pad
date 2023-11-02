def solution():
    """Jonathan's full name contains 8 letters for the first name and 10 letters for the surname. His sister's name has 5 letters for the first name and 10 letters for the second name. What's the total number of letters in their names?"""
    # Define the number of letters in Jonathan's name
    jonathan_first = 8
    jonathan_last = 10

    # Define the number of letters in Jonathan's sister's name
    sister_first = 5
    sister_last = 10

    # Calculate the total number of letters in both names
    total_letters = jonathan_first + jonathan_last + sister_first + sister_last

    # return the result
    result = total_letters
    return result

print(solution())