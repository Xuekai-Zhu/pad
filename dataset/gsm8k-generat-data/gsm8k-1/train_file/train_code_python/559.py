def solution():
    """The student council sells scented erasers in the morning before school starts to help raise money for school dances. The local bookstore donated 48 boxes of erasers. There are 24 erasers in each box. If the student council sells the erasers for $0.75 each, how much money will they make?"""
    boxes_of_erasers = 48
    erasers_per_box = 24
    total_erasers = boxes_of_erasers * erasers_per_box
    eraser_price = 0.75
    money_made = total_erasers * eraser_price
    result = money_made
    return result

print(solution())