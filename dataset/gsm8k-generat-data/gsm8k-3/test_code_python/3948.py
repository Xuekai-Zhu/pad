def solution():
    """John started weightlifting when he was 16.  When he first started he could Clean & Jerk 80 kg and he could Snatch 50 kg.  He manages to double his clean and jerk and increase his snatch by 80%.  What is his new combined total lifting capacity?"""
    
    # Define John's initial lifting capacity 
    clean_jerk = 80
    snatch = 50
    
    # Calculate John's new lifting capacity
    clean_jerk_new = clean_jerk * 2
    snatch_new = snatch * 1.8
    
    # Calculate John's total new lifting capacity
    total_new = clean_jerk_new + snatch_new
    
    # Display John's total new lifting capacity
    result = total_new
    return result

print(solution())