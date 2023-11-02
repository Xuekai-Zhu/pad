def solution():
    job1_toilets = 3
    job1_sinks = 3
    job2_toilets = 2
    job2_sinks = 5
    job3_toilets = 1
    job3_showers = 2
    job3_sinks = 3

    sink_cost = 30
    shower_cost = 40
    toilet_cost = 50

    # Calculate the potential earnings for each job
    job1_earnings = (job1_toilets * toilet_cost) + (job1_sinks * sink_cost)
    job2_earnings = (job2_toilets * toilet_cost) + (job2_sinks * sink_cost)
    job3_earnings = (job3_toilets * toilet_cost) + (job3_showers * shower_cost) + (job3_sinks * sink_cost)

    # Find the job with the highest earnings
    max_earnings = max(job1_earnings, job2_earnings, job3_earnings)

    result = max_earnings
    return result

print(solution())