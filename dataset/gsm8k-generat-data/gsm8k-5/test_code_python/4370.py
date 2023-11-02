def solution():
    # Number of apples they picked in the first round
    apples_first_round = 400

    # Number of apples they picked in the second round
    apples_second_round = (3 / 4) * apples_first_round

    # Total number of apples picked by each person
    total_apples = apples_first_round + apples_second_round + 600

    # Target number of apples they were supposed to pick
    target_apples = total_apples * 2
    result = target_apples
    return result

print(solution())