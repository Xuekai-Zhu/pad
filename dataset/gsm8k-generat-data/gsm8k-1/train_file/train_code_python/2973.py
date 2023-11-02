def solution():
    """James wants to learn to become a chess grandmaster. It takes 2 hours to learn the rules. It then takes him 49 times that long to get a level of proficiency to start playing in local tournaments. After that, he devotes his life to chess and spends 100 times as much as the combined time to get proficient to becoming a master. How much total time did he spend?"""
    time_to_learn_rules = 2
    time_to_get_proficient = 49 * time_to_learn_rules
    time_to_become_master = 100 * (time_to_learn_rules + time_to_get_proficient)
    total_time = time_to_learn_rules + time_to_get_proficient + time_to_become_master
    result = total_time
    return result

print(solution())