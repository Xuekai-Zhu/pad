def solution():
    """In one week, Jake can eat 3 papayas, his brother can eat 5 papayas, and his father can eat 4 papayas. To account for 4 weeks, how many papayas does Jake need to buy from the farmer's market?"""
    # Define the number of papayas each person eats per week
    jake_papayas = 3
    brother_papayas = 5
    father_papayas = 4

    # Calculate the total number of papayas eaten in one week
    total_papayas = jake_papayas + brother_papayas + father_papayas

    # Calculate the total number of papayas needed for 4 weeks
    total_papayas *= 4

    result = total_papayas
    return result

print(solution())