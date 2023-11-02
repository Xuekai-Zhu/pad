def solution():
    # Define the variables
    class_size = 30
    min_average = 0.75
    original_total = class_size * 0.74

    # Calculate the minimum score William needs to achieve the pizza party
    needed_score = (class_size * min_average) - original_total
    result = needed_score / (1 - (1/class_size))
    return result

print(solution())