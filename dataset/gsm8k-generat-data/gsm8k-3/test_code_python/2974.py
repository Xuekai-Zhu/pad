def solution():
    """James wants to learn to become a chess grandmaster.  It takes 2 hours to learn the rules.  It then takes him 49 times that long to get a level of proficiency to start playing in local tournaments.  After that, he devotes his life to chess and spends 100 times as much as the combined time to get proficient to becoming a master.  How much total time did he spend?"""
    # Time to learn the rules
    time_rules = 2

    # Time to get proficient enough to play in local tournaments
    time_proficient = time_rules * 49

    # Time to become a master
    time_master = (time_rules + time_proficient) * 100

    # Total time spent
    total_time = time_rules + time_proficient + time_master

    # Display the total time spent
    result = total_time
    return result

print(solution())