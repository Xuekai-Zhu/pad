def solution():
    total_apples = 85
    num_wormy_apples = total_apples / 5
    num_bruised_apples = num_wormy_apples + 9

    num_unbruised_apples = total_apples - num_wormy_apples - num_bruised_apples
    result = num_unbruised_apples
    return result

print(solution())