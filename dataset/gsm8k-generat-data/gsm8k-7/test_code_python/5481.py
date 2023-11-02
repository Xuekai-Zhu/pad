def solution():
    grace_pastries = 30
    phoebe_pastries = grace_pastries - 5
    calvin_pastries = phoebe_pastries - 8
    frank_pastries = calvin_pastries - 8
    total_pastries = grace_pastries + phoebe_pastries + calvin_pastries + frank_pastries
    result = total_pastries
    return result

print(solution())