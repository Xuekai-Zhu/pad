def solution():
    """There are 7 mL of solution in each of 6 test tubes. Dr. Igor takes all of the solution and then evenly distributes it into 3 beakers. How many mL of solution are in each beaker?"""
    # Define the number of test tubes, and the amount of solution in each
    test_tubes = 6
    solution_per_tube = 7

    # Calculate the total amount of solution
    total_solution = test_tubes * solution_per_tube

    # Divide the total amount of solution evenly among the beakers
    solution_per_beaker = total_solution / 3

    # return the result
    result = solution_per_beaker
    return result

print(solution())