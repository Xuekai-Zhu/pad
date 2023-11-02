def solution():
    """Brian can only hold his breath underwater for 10 seconds. He wants to get better, so he starts practicing. After a week, he's doubled the amount of time he can do it. After another week, he's doubled it again from the previous week. The final week, he's increased it by 50% from the previous week. How long can Brian hold his breath for now?"""
    # Define the initial breath-holding time
    time = 10
    
    # Double his time for the first week
    time *= 2
    
    # Double his time again for the second week
    time *= 2
    
    # Increase his time by 50% for the third week
    time *= 1.5
    
    # Round the time to the nearest second
    time = round(time)
    
    # Return the final breath-holding time
    result = time
    return result

print(solution())