def solution():
    # Define the stadium capacity
    capacity = 2000

    # Calculate the number of people in the stadium when it is 3/4 full
    num_people_3_4_full = 0.75 * capacity

    # Calculate the total entry fees collected when the stadium is 3/4 full
    total_fees_3_4_full = num_people_3_4_full * 20

    # Calculate the total entry fees collected when the stadium is full
    total_fees_full = capacity * 20

    # Calculate the difference between the two total entry fees collected
    difference = total_fees_full - total_fees_3_4_full
    result = difference
    return result

print(solution())