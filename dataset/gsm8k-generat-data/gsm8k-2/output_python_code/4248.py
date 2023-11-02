def solution():
    """Courtney liked to collect marbles. She kept them in mason jars. One jar had 80 marbles. Her second jar had twice that amount. She just started her third jar which currently has 1/4 the amount of her first jar. How many marbles does she have in total?"""
    first_jar = 80
    second_jar = 2 * first_jar
    third_jar = first_jar / 4
    total_marbles = first_jar + second_jar + third_jar
    result = total_marbles
    return result

print(solution())