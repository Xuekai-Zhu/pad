def solution():
    # Calculate number of shoes tried on at first store
    shoes_at_first_store = 7

    # Calculate number of shoes tried on at second store
    shoes_at_second_store = shoes_at_first_store + 2

    # Calculate total number of shoes tried on at first and second stores
    total_at_first_two_stores = shoes_at_first_store + shoes_at_second_store

    # Calculate number of shoes tried on at fourth store
    shoes_at_fourth_store = total_at_first_two_stores * 2

    # Calculate total number of shoes tried on
    total_shoes_tried_on = shoes_at_first_store + shoes_at_second_store + shoes_at_fourth_store

    result = total_shoes_tried_on
    return result

print(solution())