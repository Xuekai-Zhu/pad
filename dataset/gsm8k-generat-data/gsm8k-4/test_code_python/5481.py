def solution():
    """Calvin and Phoebe each have 8 more pastries than Frank but only five less than Grace. If Grace has 30 pastries, calculate the total number of pastries that the four have?"""
    # Define the number of pastries Grace has
    grace_pastries = 30

    # Calculate the number of pastries Calvin and Phoebe have
    calvin_phoebe_pastries = grace_pastries - 5

    # Calculate the number of pastries Frank has
    frank_pastries = (calvin_phoebe_pastries - 8) / 2

    # Calculate the total number of pastries the four have
    total_pastries = grace_pastries + calvin_phoebe_pastries + frank_pastries

    # return the result
    result = total_pastries
    return result

print(solution())