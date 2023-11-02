def solution():
    """At the polar bear club, Jerry and his three friends, Elaine, George, and Kramer, took turns jumping into a swimming pool filled with freezing-cold water. Jerry was in the pool for 3 minutes before becoming too cold to remain in the cold water. Elaine stayed in the pool for twice as long as Jerry. George could only stay in the pool for one-third as long as Elaine. And Kramer, who accidentally locked himself in the bathroom, could not find the pool. What is the combined total of minutes that Jerry and his friends were in the cold water?"""
    
    # Calculate the time Jerry spent in the pool
    jerry_time = 3
    
    # Calculate the time Elaine spent in the pool
    elaine_time = jerry_time * 2
    
    # Calculate the time George spent in the pool
    george_time = elaine_time / 3
    
    # Calculate the total time all of them spent in the pool
    total_time = jerry_time + elaine_time + george_time
    
    # Return the result
    result = total_time
    return result

print(solution())