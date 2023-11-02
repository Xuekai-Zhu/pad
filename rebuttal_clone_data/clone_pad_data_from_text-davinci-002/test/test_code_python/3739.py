def solution():
    pairs_of_shoes_first_store = 7
    pairs_of_shoes_second_store = pairs_of_shoes_first_store + 2
    pairs_of_shoes_fourth_store = (pairs_of_shoes_first_store + pairs_of_shoes_second_store) * 2
    total_pairs_of_shoes = pairs_of_shoes_first_store + pairs_of_shoes_second_store + pairs_of_shoes_fourth_store
    result = total_pairs_of_shoes
    return result

print(solution())