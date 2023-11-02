def solution():
    # Calculate the total amount of tape needed for the 5 rectangular boxes
    rectangle_tape = 5 * (30 + 2*15)

    # Calculate the total amount of tape needed for the 2 square boxes
    square_tape = 2 * (40 + 2*40)

    # Calculate the total amount of tape needed
    total_tape = rectangle_tape + square_tape
    result = total_tape
    return result

print(solution())