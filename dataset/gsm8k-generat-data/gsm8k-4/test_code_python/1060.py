def solution():
    """Barbie enjoys buying jewelry. One day, she bought 12 pairs of earrings, and gave half of them to Alissa, making Alissa's total number of collections to be triple the number of earrings she was given. How many earrings does Alissa have now?"""
    # Define the initial number of earrings
    initial_earrings = 12

    # Calculate the number of earrings given to Alissa
    alissa_earrings = initial_earrings / 2

    # Calculate the total number of earrings that Alissa has now
    alissa_total = alissa_earrings * 3

    # return the result
    result = alissa_total
    return result

print(solution())