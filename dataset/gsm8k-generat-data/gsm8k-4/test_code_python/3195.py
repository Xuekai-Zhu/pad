def solution():
    """James buys 5 packs of sodas that are 12 sodas each. He had 10 sodas already. He finishes all the sodas in 1 week. How many sodas does he drink a day?"""
    # Calculate the total number of sodas purchased
    sodas_purchased = 5 * 12

    # Calculate the total number of sodas consumed
    sodas_consumed = sodas_purchased + 10

    # Calculate the average number of sodas consumed per day
    sodas_per_day = sodas_consumed / 7

    # return the result
    result = sodas_per_day
    return result

print(solution())