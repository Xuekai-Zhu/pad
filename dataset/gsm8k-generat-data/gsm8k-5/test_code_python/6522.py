def solution():
    first_throw = 1
    second_throw = first_throw + 2
    third_throw = second_throw * 2
    fourth_throw = third_throw - 3
    fifth_throw = 8

    # Calculate the total number of skips across all throws
    total_skips = first_throw + second_throw + third_throw + fourth_throw + fifth_throw
    result = total_skips
    return result

print(solution())