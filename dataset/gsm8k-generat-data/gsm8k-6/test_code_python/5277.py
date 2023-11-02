def solution():
    # Calculate the number of ripe apples they picked
    ripe_apples = 34 - 6  # they picked 34 apples, but 6 are not ripe
    pies = ripe_apples // 4  # each pie needs 4 apples
    result = pies
    return result

print(solution())