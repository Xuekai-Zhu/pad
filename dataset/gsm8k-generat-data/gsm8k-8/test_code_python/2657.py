def solution():
    # Define the number of doughnuts in a box
    doughnuts_per_box = 2*12

    # Subtract the number of doughnuts eaten from the total number in the box
    doughnuts_left = doughnuts_per_box - 8
    result = doughnuts_left
    return result

print(solution())