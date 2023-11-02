def solution():
    """A plumber is trying to decide which of three different jobs he should take to make the most money. The first job involves fixing three toilets and three sinks at an apartment complex. The second involves two toilets and five sinks at a different apartment complex. The third involves fixing one toilet, two showers and three sinks at a third apartment complex. If the plumber charges $30 to fix a sink, $40 to fix a shower and $50 to fix a toilet, what is the most money the plumber can earn if he can only choose one of these three jobs?"""
    job1 = (3 * 50) + (3 * 30)
    job2 = (2 * 50) + (5 * 30)
    job3 = (1 * 50) + (2 * 40) + (3 * 30)
    max_money = max(job1, job2, job3)
    result = max_money
    return result

print(solution())