def solution():
    # Calculate the remaining length of sub needed after purchasing two 8 inch subs
    remaining_sub_length = 81 - (2 * 8)

    # Calculate the number of 5 inch subs needed to make up the remaining sub length
    num_5_inch_subs = remaining_sub_length // 5

    result = num_5_inch_subs
    return result

print(solution())