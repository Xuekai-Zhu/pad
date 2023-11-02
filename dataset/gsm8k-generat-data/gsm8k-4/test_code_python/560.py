def solution():
    """The student council sells scented erasers in the morning before school starts to help raise money for school dances. The local bookstore donated 48 boxes of erasers. There are 24 erasers in each box. If the student council sells the erasers for $0.75 each, how much money will they make?"""
    # Define the number of boxes of erasers donated and the number of erasers in each box
    boxes_of_erasers = 48
    erasers_per_box = 24

    # Calculate the total number of erasers
    total_erasers = boxes_of_erasers * erasers_per_box

    # Calculate the total amount of money made from selling the erasers
    total_money = total_erasers * 0.75

    result = total_money
    return result

print(solution())