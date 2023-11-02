def solution():
    """Two teams are playing in a stadium with a capacity of 2000 people. The total number of people in the stadium is 3/4 of the total capacity and each person paid $20 in entry fees. What is the difference between the total amount of fees collected when the stadium was 3/4 full and if the stadium would have been full?"""
    # Define the capacity of the stadium and the entry fee
    capacity = 2000
    entry_fee = 20

    # Calculate the total number of people in the stadium when it is 3/4 full
    total_people_3_4 = 0.75 * capacity

    # Calculate the total number of people in the stadium when it is full
    total_people_full = capacity

    # Calculate the total fees collected when the stadium is 3/4 full
    fees_3_4 = total_people_3_4 * entry_fee

    # Calculate the total fees collected when the stadium is full
    fees_full = total_people_full * entry_fee

    # Calculate the difference in fees collected
    difference = fees_full - fees_3_4

    # Display the difference in fees collected
    result = difference
    return result

print(solution())