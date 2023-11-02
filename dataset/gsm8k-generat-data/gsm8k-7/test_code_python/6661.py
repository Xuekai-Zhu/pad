def solution():
    store1_shoes = 7
    store2_shoes = store1_shoes + 2
    store3_shoes = 0
    store4_shoes = 2 * (store1_shoes + store2_shoes + store3_shoes)

    total_shoes_tried_on = store1_shoes + store2_shoes + store3_shoes + store4_shoes
    result = total_shoes_tried_on
    return result

print(solution())