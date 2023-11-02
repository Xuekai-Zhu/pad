def solution():
    """In one week, Jake can eat 3 papayas, his brother can eat 5 papayas, and his father can eat 4 papayas.  To account for 4 weeks, how many papayas does Jake need to buy from the farmer’s market?"""
    # Define the number of papayas each person can eat in a week
    JAKE_PAPAYAS = 3
    BROTHER_PAPAYAS = 5
    FATHER_PAPAYAS = 4

    # Define the number of weeks for which to account
    WEEKS = 4

    # Calculate the total number of papayas needed
    total_papayas = (JAKE_PAPAYAS + BROTHER_PAPAYAS + FATHER_PAPAYAS) * WEEKS

    # Display the total number of papayas needed
    result = total_papayas
    return result

print(solution())