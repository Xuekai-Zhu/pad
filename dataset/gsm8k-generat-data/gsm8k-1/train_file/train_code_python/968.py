def solution():
    """Lake Crystal has twenty percent fewer frogs than Lassie Lake. If Lassie Lake has forty-five frogs, how many frogs are there in total in the two lakes?"""
    lassie_frogs = 45
    crystal_frogs = lassie_frogs - (lassie_frogs * 0.2)
    total_frogs = lassie_frogs + crystal_frogs
    result = total_frogs
    return result

print(solution())