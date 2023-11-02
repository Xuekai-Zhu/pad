def solution():
    total_problems = 75  # Georgia has 75 problems to solve
    problems_solved = 10  # Georgia has completed 10 problems after 20 minutes
    problems_solved += 2 * (20 / 60) * 75 / 4  # Georgia has completed twice as many problems after another 20 minutes
    remaining_time = 40 / 60  # Georgia has 40 minutes left to complete the test
    problems_solved += remaining_time * 75 / 4  # Georgia solves a quarter of the remaining problems every minute

    # Calculate the number of problems Georgia has left to solve
    problems_left = total_problems - problems_solved
    result = problems_left
    return result

print(solution())