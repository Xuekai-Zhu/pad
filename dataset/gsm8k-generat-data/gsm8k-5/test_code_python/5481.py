def solution():
    grace_pastries = 30  # Grace has 30 pastries
    calvin_pastries = grace_pastries - 5 - 8  # Calvin has 5 less than Grace and 8 more than Frank
    phoebe_pastries = grace_pastries - 5 - 8  # Phoebe also has 5 less than Grace and 8 more than Frank
    frank_pastries = (grace_pastries - 8) / 2  # Frank has 8 less than Calvin and Phoebe, and they each have 8 more than him

    # Calculate the total number of pastries the four have
    total_pastries = grace_pastries + calvin_pastries + phoebe_pastries + frank_pastries
    result = total_pastries
    return result

print(solution())