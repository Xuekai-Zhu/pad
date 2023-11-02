def solution():
    """There were 10 snowflakes at first. It snowed an additional 4 snowflakes every 5 minutes. How many minutes passed before there were 58 snowflakes?"""
    initial_snowflakes = 10
    snowflakes_needed = 58
    snowflakes_per_interval = 4
    minutes_per_interval = 5
    
    # Calculate number of intervals needed
    intervals_needed = (snowflakes_needed - initial_snowflakes) / snowflakes_per_interval
    
    # Calculate total minutes needed
    total_minutes = intervals_needed * minutes_per_interval
    
    result = total_minutes
    return result

print(solution())