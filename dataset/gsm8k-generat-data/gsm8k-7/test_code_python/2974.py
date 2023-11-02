def solution():
    rule_learning_time = 2
    proficiency_learning_time = 49 * rule_learning_time
    mastery_learning_time = 100 * (rule_learning_time + proficiency_learning_time)

    total_learning_time = rule_learning_time + proficiency_learning_time + mastery_learning_time
    result = total_learning_time
    return result

print(solution())