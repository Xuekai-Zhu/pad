def solution():
    """Mother made 2 dozen brownies and placed them on the kitchen counter to cool. Father smelled the brownies, came into the kitchen and ate 8 of them. Then, their daughter, Mooney, wandered into the kitchen and ate 4 of the brownies. The next morning, Mother made another two dozen brownies and added them to those remaining from the day before. After that, how many brownies were on the counter?"""
    brownies_on_counter = 2 * 12 
    brownies_on_counter -= 8 
    brownies_on_counter -= 4
    brownies_on_counter += 2 * 12
    result = brownies_on_counter
    return result

print(solution())