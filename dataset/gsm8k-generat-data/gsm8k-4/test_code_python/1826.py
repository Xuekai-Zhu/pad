def solution():
    """Miriam is trying to exercise more and figures if she counts her exercises it will be encouraging to see her numbers go up. 
    On Monday she does 5 push-ups. On Tuesday she does 7 push-ups. On Wednesday she does twice as many push-ups as the day before. 
    On Thursday she does half the number of total pushups she already did that week. Finally, on Friday 
    she does as many pushups as the total number she did over the previous four days. 
    How many pushups does Miriam do on Friday?"""
    
    # Define the number of push-ups each day
    pushup_mon = 5
    pushup_tue = 7
    pushup_wed = pushup_tue * 2
    pushup_thu = (pushup_mon + pushup_tue + pushup_wed) / 2
    pushup_fri = pushup_mon + pushup_tue + pushup_wed + pushup_thu
    
    result = pushup_fri
    return result

print(solution())