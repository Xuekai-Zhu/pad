def solution():
    # Calculate the number of skips for each throw
    first_throw = 0
    second_throw = first_throw + 2
    third_throw = second_throw * 2
    fourth_throw = third_throw - 3
    fifth_throw = fourth_throw + 1

    # Calculate the total number of skips
    total_skips = first_throw + second_throw + third_throw + fourth_throw + fifth_throw

    result = total_skips
    return result

print(solution())