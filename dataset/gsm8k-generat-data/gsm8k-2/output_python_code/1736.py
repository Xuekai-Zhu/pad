def solution():
    """At the polar bear club, Jerry and his three friends, Elaine, George, and Kramer, took turns jumping into a swimming pool filled with freezing-cold water. Jerry was in the pool for 3 minutes before becoming too cold to remain in the cold water. Elaine stayed in the pool for twice as long as Jerry. George could only stay in the pool for one-third as long as Elaine. And Kramer, who accidentally locked himself in the bathroom, could not find the pool. What is the combined total of minutes that Jerry and his friends were in the cold water?"""
    jerry_time = 3
    elaine_time = 2 * jerry_time
    george_time = elaine_time / 3
    kramer_time = 0
    total_time = jerry_time + elaine_time + george_time + kramer_time
    result = total_time
    return result

print(solution())