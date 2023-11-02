def solution():
    # Calculate the earning potential for each job
    job1_earnings = (3 * 50) + (3 * 30)  # Three toilets and three sinks
    job2_earnings = (2 * 50) + (5 * 30)  # Two toilets and five sinks
    job3_earnings = (1 * 50) + (2 * 40) + (3 * 30)  # One toilet, two showers, and three sinks

    # Determine the maximum earning potential among the three jobs
    max_earnings = max(job1_earnings, job2_earnings, job3_earnings)
    result = max_earnings
    return result

print(solution())