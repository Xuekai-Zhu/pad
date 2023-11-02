def solution():
    total_inches = 81  # Venus needs 81 inches of sub
    purchased_inches = 2 * 8  # Venus already bought two 8 inch subs
    remaining_inches = total_inches - purchased_inches  # Venus needs to buy more subs to reach the total inches required
    small_sub_inches = 5  # The shop sells 5 inch subs

    # Calculate the number of 5 inch subs Venus needs to buy
    num_small_subs = remaining_inches // small_sub_inches
    result = num_small_subs
    return result

print(solution())