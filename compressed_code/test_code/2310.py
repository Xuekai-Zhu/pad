def solution():
    
    rule_time = 2
    proficiency_time = rule_time * 49
    master_time = (rule_time + proficiency_time) * 100
    total_time = rule_time + proficiency_time + master_time
    result = total_time
    return result

print(solution())