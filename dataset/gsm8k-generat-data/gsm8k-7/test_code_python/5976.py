def solution():
    needed_sub_length = 81
    eight_inch_subs = 2
    eight_inch_sub_length = 8
    five_inch_sub_length = 5

    # Calculate the total length of the two 8 inch subs
    total_eight_sub_length = eight_inch_subs * eight_inch_sub_length

    # Calculate the remaining length needed for the party
    remaining_sub_length = needed_sub_length - total_eight_sub_length

    # Calculate the number of 5 inch subs needed to make up the remaining length
    num_five_inch_subs = remaining_sub_length / five_inch_sub_length
    result = num_five_inch_subs
    return result

print(solution())