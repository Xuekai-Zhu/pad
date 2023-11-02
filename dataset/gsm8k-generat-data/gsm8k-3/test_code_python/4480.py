def solution():
    """A pipe is clogged so that only 2 ounces of cleaner can run through the pipe per minute. 
    After fifteen minutes, the cleaner has unclogged it enough that 3 ounces can run through per minute. 
    Ten minutes later, the clog is cleared enough for 4 ounces to run through per minute. 
    How many ounces of cleaner were used after 30 minutes?"""
    
    # Calculate the amount of cleaner used in the first 15 minutes
    cleaner_used_15 = 2 * 15  # 2 ounces per minute for 15 minutes

    # Calculate the amount of cleaner used in the next 10 minutes
    cleaner_used_10 = 3 * 10  # 3 ounces per minute for 10 minutes

    # Calculate the amount of cleaner used in the last 5 minutes
    cleaner_used_5 = 4 * 5  # 4 ounces per minute for 5 minutes

    # Calculate the total amount of cleaner used
    total_cleaner_used = cleaner_used_15 + cleaner_used_10 + cleaner_used_5

    # Display the total amount of cleaner used
    result = total_cleaner_used
    return result

print(solution())