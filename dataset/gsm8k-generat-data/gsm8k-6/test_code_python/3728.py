def solution():
    # Calculate the total time Marcus spends on the calzones
    saute_onions_time = 20
    saute_garlic_peppers_time = saute_onions_time / 4
    knead_dough_time = 30
    let_rest_time = knead_dough_time * 2
    knead_and_rest_time = knead_dough_time + let_rest_time
    assemble_calzones_time = knead_and_rest_time / 10
    total_time = saute_onions_time + saute_garlic_peppers_time + knead_dough_time + let_rest_time + assemble_calzones_time
    result = total_time
    return result

print(solution())