def solution():
    # Calculate the number of problems Georgia has completed after 40 minutes
    problems_completed = 10 + 2 * 10  # Georgia completed 10 problems in the first 20 minutes, and 20 problems in the next 20 minutes (twice as many)
    time_left = 40  # minutes she has left to complete the rest of the test
    avg_time_per_problem = time_left / (75 - problems_completed)  # calculate average time she can spend on each remaining problem
    problems_left = round(time_left / avg_time_per_problem)  # round to the nearest whole number
    result = problems_left
    return result

print(solution())