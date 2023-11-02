def solution():
    boxes = 48  # The student council received 48 boxes of erasers
    erasers_per_box = 24  # There are 24 erasers in each box
    eraser_price = 0.75  # The student council sells each eraser for $0.75

    # Calculate the total number of erasers
    total_erasers = boxes * erasers_per_box

    # Calculate the total amount of money made by selling the erasers
    total_money = total_erasers * eraser_price
    result = total_money
    return result

print(solution())