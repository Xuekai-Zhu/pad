def solution():
    """Georgie needs 3 avocados to make her grandmother's guacamole recipe. If she already had 5 avocados and her sister buys another 4 avocados, how many servings of guacamole can Georgie make?"""
    avocados_needed_per_serving = 3
    total_avocados = 5 + 4
    servings = total_avocados // avocados_needed_per_serving
    result = servings
    return result

print(solution())