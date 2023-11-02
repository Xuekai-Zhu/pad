def solution():
    """James wants to learn to become a chess grandmaster. It takes 2 hours to learn the rules. It then takes him 49 times that long to get a level of proficiency to start playing in local tournaments. After that, he devotes his life to chess and spends 100 times as much as the combined time to get proficient to becoming a master. How much total time did he spend?"""
    
    # Calculate the time to become proficient
    proficient_time = 2 + 49 * 2
    
    # Calculate the time to become a master
    master_time = 100 * proficient_time
    
    # Calculate the total time spent
    total_time = 2 + proficient_time + master_time
    
    result = total_time
    return result

print(solution())