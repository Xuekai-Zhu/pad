def solution():
    """Building A has 4 floors, which is 9 less than Building B. Building C has six less than five times as many floors as Building B. How many floors does Building C have?"""
    # Define the number of floors in Building A
    floors_A = 4

    # Calculate the number of floors in Building B
    floors_B = floors_A + 9

    # Calculate five times the number of floors in Building B
    five_times_floors_B = floors_B * 5

    # Calculate the number of floors in Building C
    floors_C = five_times_floors_B - 6

    # return the result
    result = floors_C
    return result

print(solution())