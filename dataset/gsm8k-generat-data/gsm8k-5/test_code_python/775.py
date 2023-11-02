def solution():
    # Number of pieces of fruit in bucket C
    fruit_C = 9

    # Number of pieces of fruit in bucket B
    fruit_B = fruit_C + 3

    # Number of pieces of fruit in bucket A
    fruit_A = fruit_B + 4

    # Total number of pieces of fruit in all three buckets
    total_fruit = fruit_C + fruit_B + fruit_A
    result = total_fruit
    return result

print(solution())