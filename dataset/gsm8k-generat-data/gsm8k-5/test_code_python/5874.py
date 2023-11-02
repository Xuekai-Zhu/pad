def solution():
    # Number of frogs in Pond A is twice that in Pond B
    # Therefore, Number of frogs in Pond B = Number of frogs in Pond A / 2
    num_frogs_pond_a = 32
    num_frogs_pond_b = num_frogs_pond_a / 2

    # Total number of frogs in both ponds is the sum of the number of frogs in Pond A and Pond B
    total_frogs = num_frogs_pond_a + num_frogs_pond_b
    result = total_frogs
    return result

print(solution())