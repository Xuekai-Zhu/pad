def solution():
    shoes_first_store = 7  # Helga tried on 7 pairs of shoes at the first store
    shoes_second_store = shoes_first_store + 2  # Helga tried on 2 more pairs at the second store
    shoes_third_store = 0  # Helga did not try on any shoes at the third store
    shoes_fourth_store = 2 * (shoes_first_store + shoes_second_store + shoes_third_store)  # Helga tried on twice as many pairs at the fourth store

    # Calculate the total number of shoes Helga tried on
    total_shoes_tried_on = shoes_first_store + shoes_second_store + shoes_third_store + shoes_fourth_store
    result = total_shoes_tried_on
    return result

print(solution())