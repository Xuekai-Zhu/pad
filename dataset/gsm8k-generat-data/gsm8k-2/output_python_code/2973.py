def solution():
    """James wants to learn to become a chess grandmaster. It takes 2 hours to learn the rules. It then takes him 49 times that long to get a level of proficiency to start playing in local tournaments. After that, he devotes his life to chess and spends 100 times as much as the combined time to get proficient to becoming a master. How much total time did he spend?"""
    rule_time = 2
    proficiency_time = rule_time * 49
    master_time = (rule_time + proficiency_time) * 100
    total_time = rule_time + proficiency_time + master_time
    result = total_time
    return result

print(solution())