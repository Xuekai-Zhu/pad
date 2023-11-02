def solution():
    num_frogs_pondA = 32
    num_frogs_pondB = num_frogs_pondA / 2 # Pond A has twice as many frogs as Pond B.

    # Calculate the total number of frogs in both ponds combined
    total_num_frogs = num_frogs_pondA + num_frogs_pondB
    result = total_num_frogs
    return result

print(solution())