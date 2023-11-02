def solution():
    # Calculate the percentage of kernels that popped in each bag
    bag1_percentage = (60 / 75) * 100
    bag2_percentage = (42 / 50) * 100
    bag3_percentage = (82 / 100) * 100

    # Calculate the average percentage of kernels that popped
    average_percentage = (bag1_percentage + bag2_percentage + bag3_percentage) / 3
    result = average_percentage
    return result

print(solution())