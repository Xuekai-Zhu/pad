def solution():
    onion_saute_time = 20
    garlic_pepper_saute_time = onion_saute_time / 4
    dough_knead_time = 30
    dough_rest_time = dough_knead_time * 2
    calzone_assemble_time = (dough_knead_time + dough_rest_time) / 10

    total_time = onion_saute_time + garlic_pepper_saute_time + dough_knead_time + dough_rest_time + calzone_assemble_time
    result = total_time
    return result

print(solution())