def solution():
    """Carlo has a music recital next week. He practiced twice as long on Monday as on Tuesday. On Tuesday, he practiced 10 minutes less than on Wednesday. On Wednesday, he practiced 5 minutes more than on Thursday. On Thursday, he practiced for 50 minutes. If he needs to practice for a total of 5 hours that week, how long should Carlo practice on Friday?"""
    # Calculate total practice time for the first 4 days
    thursday_time = 50
    wednesday_time = thursday_time + 5
    tuesday_time = wednesday_time - 10
    monday_time = 2 * tuesday_time
    
    total_time = monday_time + tuesday_time + wednesday_time + thursday_time
    
    # Calculate remaining time for Friday
    target_time = 5 * 60 # 5 hours in minutes
    friday_time = target_time - total_time
    
    result = friday_time
    return result

print(solution())