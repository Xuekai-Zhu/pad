def solution():
    """A plumber is trying to decide which of three different jobs he should take to make the most money.  The first job involves fixing three toilets and three sinks at an apartment complex.  The second involves two toilets and five sinks at a different apartment complex.  The third involves fixing one toilet, two showers and three sinks at a third apartment complex.  If the plumber charges $30 to fix a sink, $40 to fix a shower and $50 to fix a toilet, what is the most money the plumber can earn if he can only choose one of these three jobs?"""
    # Define the prices for each type of repair
    TOILET_PRICE = 50
    SINK_PRICE = 30
    SHOWER_PRICE = 40

    # Calculate the total earnings for each job
    job1_earnings = 3 * TOILET_PRICE + 3 * SINK_PRICE
    job2_earnings = 2 * TOILET_PRICE + 5 * SINK_PRICE
    job3_earnings = 1 * TOILET_PRICE + 2 * SHOWER_PRICE + 3 * SINK_PRICE

    # Determine which job has the highest earnings
    max_earnings = max(job1_earnings, job2_earnings, job3_earnings)

    # Display the maximum earnings
    result = max_earnings
    return result

print(solution())