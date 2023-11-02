def solution():
    """Freddy is 2 years younger than Stephanie. Stephanie is 4 times as old as Job. If Job is 5, how old is Freddy?"""
    job_age = 5
    stephanie_age = 4 * job_age
    freddy_age = stephanie_age - 2
    result = freddy_age
    return result

print(solution())