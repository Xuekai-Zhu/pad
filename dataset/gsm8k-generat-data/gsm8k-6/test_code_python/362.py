def solution():
    tote_weight = 8  # given tote weight

    # Find Kevin's briefcase weight when it's empty and when it's full with laptop and work papers
    briefcase_empty = tote_weight / 2
    briefcase_full = (2 * tote_weight) + (6 * briefcase_empty)

    # Find the weight difference between Kevin's briefcase and Karen's tote
    weight_difference = briefcase_full - tote_weight

    # Find the weight of Kevin's laptop
    laptop_weight = weight_difference / 3  # since the work papers are 1/6 of the full briefcase weight

    result = laptop_weight - tote_weight
    return result

print(solution())