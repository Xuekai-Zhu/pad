def solution():
    # Find the number of pastries that Grace has
    grace_pastries = 30

    # Find the number of pastries that both Calvin and Phoebe have
    calvin_phoebe_pastries = grace_pastries - 5

    # Find the number of pastries that Frank has
    frank_pastries = calvin_phoebe_pastries - 8

    # Calculate the total number of pastries that the four have
    total_pastries = grace_pastries + calvin_phoebe_pastries + frank_pastries + calvin_phoebe_pastries

    result = total_pastries
    return result

print(solution())