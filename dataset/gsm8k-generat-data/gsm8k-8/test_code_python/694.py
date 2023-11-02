def solution():
    # Calculate the total number of engines
    total_engines = 5 * 80

    # Calculate the number of defective engines
    defective_engines = total_engines / 4

    # Calculate the number of non-defective engines
    non_defective_engines = total_engines - defective_engines
    result = non_defective_engines
    return result

print(solution())