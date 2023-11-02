def solution():
    """The student council sells scented erasers in the morning before school starts to help raise money for school dances. The local bookstore donated 48 boxes of erasers. There are 24 erasers in each box. If the student council sells the erasers for $0.75 each, how much money will they make?"""
    # Define the number of erasers in each box and the number of boxes donated
    ERASERS_PER_BOX = 24
    BOXES_DONATED = 48

    # Calculate the total number of erasers donated
    total_erasers = ERASERS_PER_BOX * BOXES_DONATED

    # Calculate the total amount of money the student council will make
    total_money = total_erasers * 0.75

    # Display the total amount of money the student council will make
    result = total_money
    return result

print(solution())