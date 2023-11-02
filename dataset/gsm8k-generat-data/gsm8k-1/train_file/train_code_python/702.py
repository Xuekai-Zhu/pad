def solution():
    """Georgie needs 3 avocados to make her grandmother's guacamole recipe. If she already had 5 avocados and her sister buys another 4 avocados, how many servings of guacamole can Georgie make?"""
    avocados_needed = 3
    avocados_owned = 5
    additional_avocados = 4
    total_avocados = avocados_owned + additional_avocados
    servings_possible = total_avocados // avocados_needed
    result = servings_possible
    return result

print(solution())