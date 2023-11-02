def solution():
    """A plumber is trying to decide which of three different jobs he should take to make the most money.  The first job involves fixing three toilets and three sinks at an apartment complex.  The second involves two toilets and five sinks at a different apartment complex.  The third involves fixing one toilet, two showers and three sinks at a third apartment complex.  If the plumber charges $30 to fix a sink, $40 to fix a shower and $50 to fix a toilet, what is the most money the plumber can earn if he can only choose one of these three jobs?"""
    # Define the prices for fixing the plumbing items
    sink_price = 30
    shower_price = 40
    toilet_price = 50

    # Calculate the potential earnings for each job
    job1_profit = 3 * sink_price + 3 * toilet_price
    job2_profit = 5 * sink_price + 2 * toilet_price
    job3_profit = 3 * sink_price + 2 * shower_price + 1 * toilet_price

    # Choose the job with the highest potential earnings
    if job1_profit >= job2_profit and job1_profit >= job3_profit:
        job = "job 1"
        profit = job1_profit
    elif job2_profit >= job1_profit and job2_profit >= job3_profit:
        job = "job 2"
        profit = job2_profit
    else:
        job = "job 3"
        profit = job3_profit

    result = profit
    return result

print(solution())