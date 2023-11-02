def solution():
    """There are 7 mL of solution in each of 6 test tubes. Dr. Igor takes all of the solution and then evenly distributes it into 3 beakers. How many mL of solution are in each beaker?"""
    solution_per_tube = 7
    total_solution = solution_per_tube * 6
    beakers = 3
    solution_per_beaker = total_solution / beakers
    result = solution_per_beaker
    return result

print(solution())