def solution():
    num_test_tubes = 6
    solution_per_tube = 7
    num_beakers = 3

    # Calculate the total amount of solution
    total_solution = num_test_tubes * solution_per_tube

    # Calculate the amount of solution in each beaker
    solution_per_beaker = total_solution / num_beakers
    result = solution_per_beaker
    return result

print(solution())