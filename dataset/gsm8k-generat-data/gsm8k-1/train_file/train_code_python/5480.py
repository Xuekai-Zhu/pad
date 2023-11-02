def solution():
    """Calvin and Phoebe each have 8 more pastries than Frank but only five less than Grace. If Grace has 30 pastries, calculate the total number of pastries that the four have?"""
    grace_pastries = 30
    frank_pastries = grace_pastries + 5 - 8
    calvin_pastries = phoebe_pastries = frank_pastries + 8
    total_pastries = grace_pastries + frank_pastries + calvin_pastries + phoebe_pastries
    result = total_pastries
    return result

print(solution())