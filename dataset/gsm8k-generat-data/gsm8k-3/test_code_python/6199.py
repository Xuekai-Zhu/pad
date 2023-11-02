def solution():
    """Building A has 4 floors, which is 9 less than Building B. Building C has six less than five times as many floors as Building B. How many floors does Building C have?"""
    # Define the number of floors in Building A and the difference between A and B
    floors_A = 4
    diff_AB = 9
    floors_B = floors_A + diff_AB

    # Define the number of floors in Building C
    floors_C = 5 * floors_B - 6

    # Display the number of floors in Building C
    result = floors_C
    return result

print(solution())