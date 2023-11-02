def solution():
    """Two teams are playing in a stadium with a capacity of 2000 people. The total number of people in the stadium is 3/4 of the total capacity and each person paid $20 in entry fees. What is the difference between the total amount of fees collected when the stadium was 3/4 full and if the stadium would have been full?"""
    # Define the capacity of the stadium
    capacity = 2000

    # Calculate the number of people in the stadium when it is 3/4 full
    three_fourth_full = capacity * (3/4)

    # Calculate the total entry fees collected when the stadium is 3/4 full
    fees_3_4_full = three_fourth_full * 20

    # Calculate the total entry fees collected when the stadium is full
    fees_full = capacity * 20

    # Calculate the difference between the two amounts
    difference = fees_full - fees_3_4_full

    result = difference
    return result

print(solution())