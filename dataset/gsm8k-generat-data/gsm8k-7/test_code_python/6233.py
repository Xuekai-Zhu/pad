def solution():
    total_children = 50
    boys_ratio = 3/5

    # Calculate the number of boys
    num_boys = total_children * boys_ratio

    # Calculate the number of girls
    num_girls = total_children - num_boys
    result = num_girls
    return result

print(solution())