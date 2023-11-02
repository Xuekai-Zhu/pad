def solution():
    """Barbie enjoys buying jewelry. One day, she bought 12 pairs of earrings, and gave half of them to Alissa, making Alissa's total number of collections to be triple the number of earrings she was given. How many earrings does Alissa have now?"""
    # Define the number of earrings Barbie bought
    earrings_bought = 12 * 2  # since each pair has two earrings

    # Calculate the number of earrings Alissa received
    earrings_received = earrings_bought / 2

    # Calculate the number of earrings Alissa has now
    earrings_now = earrings_received * 3

    # Display the number of earrings Alissa has now
    result = earrings_now
    return result

print(solution())