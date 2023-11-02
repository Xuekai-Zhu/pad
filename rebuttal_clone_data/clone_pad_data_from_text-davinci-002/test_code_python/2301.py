def solution():
    initial_snowflakes = 10
    snowflakes_added = 4
    minutes_between_additions = 5
    total_snowflakes = 58
    
    minutes_passed = (total_snowflakes - initial_snowflakes) / snowflakes_added * minutes_between_additions 
    result = minutes_passed
    
    return result

print(solution())