def solution():
    """Paul is collecting license plates from different states. He has plates from 40 different states. 
    For each percentage point of total US states that he has, his parents will give him $2. How much does he earn from them?"""
    
    # Define the total number of US states
    TOTAL_STATES = 50
    
    # Calculate the percentage of US states Paul has license plates from
    percentage = (40 / TOTAL_STATES) * 100
    
    # Calculate the amount Paul will earn from his parents
    earnings = percentage * 2
    
    # Display the earnings
    result = earnings
    return result

print(solution())